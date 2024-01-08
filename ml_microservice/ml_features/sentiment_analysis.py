import json
import logging
import os
import socket
import string
from uuid import UUID

import aiokafka
from dotenv import load_dotenv
from transformers import pipeline

os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

load_dotenv("../.env")
KAFKA_RESPONSE_TOPIC = os.getenv('KAFKA_SENTIMENT_ANALYSIS_RESPONSE')
KAFKA_REQUEST_TOPIC = os.getenv('KAFKA_SENTIMENT_ANALYSIS_REQUEST')


class SentimentAnalyser:
    def __init__(self, model="lxyuan/distilbert-base-multilingual-cased-sentiments-student"):
        self.__classifier__ = pipeline(
            model=model,
            top_k=None
        )
        self.__consumer__ = None
        self.__producer__ = None

    async def initialize(self):
        self.__consumer__ = aiokafka.AIOKafkaConsumer(
            KAFKA_REQUEST_TOPIC,
            group_id='sentiment-analysis_consumer',
            bootstrap_servers='kafka:9092'
        )
        self.__producer__ = aiokafka.AIOKafkaProducer(
            bootstrap_servers='kafka:9092', client_id=socket.gethostname())

    async def __produce_analysis__(self, text: string, uuid):
        result = max(self.__classifier__(text)[0], key=lambda x: x['score'])
        byte_value = json.dumps(result).encode("utf-8")
        byte_key = str(uuid).encode("utf-8")
        try:
            print("Sentiment Analysis: Key: " + str(byte_key) + ", Value: " + str(byte_value))
            await self.__producer__.send(topic=KAFKA_RESPONSE_TOPIC, key=byte_key, value=byte_value)
        except Exception as e:
            print(f"Error sending message: {e}")

    async def consume(self):
        await self.__consumer__.start()
        await self.__producer__.start()
        try:
            async for msg in self.__consumer__:
                text = msg.value.decode('utf-8')
                uuid = msg.key.decode('utf-8')
                print("(SA) Consuming UUID: " + str(uuid) + ", Message: " + text)
                await self.__produce_analysis__(text=text, uuid=uuid)
        except Exception as e:
            print(f"Unexpected error trying to consume messages: {e}")
        finally:
            await self.__consumer__.stop()
            await self.__producer__.stop()
