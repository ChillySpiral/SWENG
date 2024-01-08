import base64
import io
import json
import logging
import os
import re
import socket
import string
from uuid import UUID
from PIL import Image

import requests
import aiokafka
from dotenv import load_dotenv
from pydantic import BaseModel

os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

load_dotenv()
KAFKA_REQUEST_TOPIC = os.getenv('KAFKA_RESIZE_REQUEST')
KAFKA_RESPONSE_TOPIC = os.getenv('KAFKA_RESIZE_RESPONSE')


class PostImage(BaseModel):
    post_id: UUID
    image: str


class UUIDEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, UUID):
            # if the obj is uuid, we simply return the value of uuid
            return obj.hex
        return json.JSONEncoder.default(self, obj)


class Resizer:
    def __init__(self):
        self.__consumer__ = None
        self.__producer__ = None

    async def initialize(self):
        self.__consumer__ = aiokafka.AIOKafkaConsumer(
            KAFKA_REQUEST_TOPIC,
            group_id='resize_consumer',
            bootstrap_servers='kafka:9092',
        )

    async def consume(self):
        await self.__consumer__.start()
        try:
            async for msg in self.__consumer__:
                text = msg.value.decode('utf-8')
                uuid = UUID(msg.key.decode('utf-8'))

                print("(RS) Consuming UUID: " + str(uuid) + ", Message: " + text)

                image = requests.get("http://server/internal/" + str(uuid))

                if not image:
                    return

                buffer = io.BytesIO()
                encoding = 'utf-8'
                encoded_image_string = image.content.decode(encoding)
                editable_image = encoded_image_string[1:-1]
                editable_image = re.sub('^data:image/.+;base64,', '', editable_image)
                editable_image = re.sub('[^a-zA-Z0-9%s]+' % '+/', '', editable_image)  # normalize
                missing_padding = len(editable_image) % 4
                if missing_padding:
                    editable_image += '=' * (4 - missing_padding)

                imgdata = base64.b64decode(editable_image)
                img = Image.open(io.BytesIO(imgdata))
                new_img = img.resize((400, 400))  # x, y
                new_img.save(buffer, format="PNG")
                img_b64 = base64.b64encode(buffer.getvalue())
                res = 'data:image/png;base64,' + img_b64.decode(encoding)

                headers = {'content-type': 'application/json'}
                obj = PostImage(post_id=uuid, image=res)
                data = json.dumps(obj.__dict__, cls=UUIDEncoder)
                print(data)
                response = requests.post("http://server/internal/", data, headers=headers)
                print(response)

        except Exception as e:
            print(f"Unexpected error trying to consume messages: {e}")
        finally:
            await self.__consumer__.stop()
