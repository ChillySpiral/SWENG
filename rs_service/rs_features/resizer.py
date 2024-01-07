import base64
import io
import json
import logging
import os
import socket
import string
from uuid import UUID
from PIL import Image

import requests
import aiokafka
from dotenv import load_dotenv

os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

load_dotenv()
KAFKA_REQUEST_TOPIC = os.getenv('KAFKA_RESIZE_REQUEST')
KAFKA_RESPONSE_TOPIC = os.getenv('KAFKA_RESIZE_RESPONSE')


class Resizer:
    def __init__(self):
        self.__consumer__ = None
        self.__producer__ = None

    async def initialize(self):
        self.__consumer__ = aiokafka.AIOKafkaConsumer(
            KAFKA_REQUEST_TOPIC,
            group_id='resize_consumer',
            bootstrap_servers='kafka:9092',
            fetch_max_bytes=20000000
        )


    async def consume(self):
        await self.__consumer__.start()
        try:
            async for msg in self.__consumer__:
                text = msg.value.decode('utf-8')
                uuid = UUID(msg.key.decode('utf-8'))

                print("(RS) Consuming UUID: " + str(uuid) + ", Message: " + text)

                image = requests.get("http://server/internal/"+str(uuid))

                if not image:
                    continue
                print(f"Image: " + str(image))

                buffer = io.BytesIO()
                imgdata = base64.b64decode(image)
                img = Image.open(io.BytesIO(imgdata))
                new_img = img.resize((2, 2))  # x, y
                new_img.save(buffer, format="PNG")
                img_b64 = base64.b64encode(buffer.getvalue())
                print(img_b64)

                #ToDo: Send Image
                obj = {'small_image': str(img_b64)}
                requests.post("http://server/internal/"+str(uuid))

        except Exception as e:
            print(f"Unexpected error trying to consume messages: {e}")
        finally:
            await self.__consumer__.stop()
