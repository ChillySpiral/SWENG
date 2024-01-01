import logging
import os
import socket
import string
from uuid import UUID

import aiokafka
from dotenv import load_dotenv
from transformers import pipeline, set_seed

os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

load_dotenv("../.env")
KAFKA_RESPONSE_TOPIC = os.getenv('KAFKA_TEXT_GENERATION_RESPONSE')
KAFKA_REQUEST_TOPIC = os.getenv('KAFKA_TEXT_GENERATION_REQUEST')


class TextGenerator:
    def __init__(self, seed=42, task="text-generation", model="gpt2"):
        self.__producer__ = None
        self.__consumer__ = None
        self.generator = pipeline(task=task, model=model)
        set_seed(seed)

    async def initialize(self):
        self.__consumer__ = aiokafka.AIOKafkaConsumer(
            KAFKA_REQUEST_TOPIC,
            bootstrap_servers='kafka:9092',
        )
        self.__producer__ = aiokafka.AIOKafkaProducer(
            bootstrap_servers='kafka:9092', client_id=socket.gethostname())

    async def __produce_analysis__(self, text: string, uuid: UUID, max_length=30, num_return_sequences=5):
        generated_text = self.generator(text, max_length=max_length,
                                        num_return_sequences=num_return_sequences)
        try:
            await self.__producer__.send(topic=KAFKA_RESPONSE_TOPIC, key=uuid, value=generated_text)
        except Exception as e:
            print(f"Error sending kafka message: {e}")

    async def consume(self):
        await self.__consumer__.start()
        await self.__producer__.start()
        try:
            async for msg in self.__consumer__:
                text = msg.value.decode('utf-8')
                uuid = UUID(msg.key.decode('utf-8'))
                await self.__produce_analysis__(text=text, uuid=uuid)
        except Exception as e:
            print(f"Unexpected error trying to consume messages: {e}")
        finally:
            await self.__consumer__.stop()
            await self.__producer__.stop()
