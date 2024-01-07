import base64
import io
import json
import logging
import os
import socket
import string
from uuid import UUID
from PIL import Image

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
            bootstrap_servers='kafka:9092'
        )

        self.__producer__ = aiokafka.AIOKafkaProducer(
            bootstrap_servers='kafka:9092', client_id=socket.gethostname())

    async def consume(self):
        await self.__consumer__.start()
        await self.__producer__.start()
        try:
            async for msg in self.__consumer__:
                text = msg.value.decode('utf-8')
                uuid = msg.key.decode('utf-8')

                print("(SA) Consuming UUID: " + str(uuid) + ", Message: " + text)
                buffer = io.BytesIO()
                imgdata = base64.b64decode(text)
                img = Image.open(io.BytesIO(imgdata))
                new_img = img.resize((2, 2))  # x, y
                new_img.save(buffer, format="PNG")
                img_b64 = base64.b64encode(buffer.getvalue())

                byte_value = img_b64
                byte_key = str(uuid).encode("utf-8")
                try:
                    print("Resize: Key: " + str(byte_key) + ", Value: " + str(byte_value))
                    await self.__producer__.send(topic=KAFKA_RESPONSE_TOPIC, key=byte_key, value=byte_value)
                except Exception as e:
                    print(f"Error sending message: {e}")
        except Exception as e:
            print(f"Unexpected error trying to consume messages: {e}")
        finally:
            await self.__consumer__.stop()
            await self.__producer__.stop()
