import json
import os
import socket
import string
import uuid
from uuid import UUID
import aiokafka
from dotenv import load_dotenv
from transformers import pipeline
from uuid_encoder import UUIDEncoder

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
        producer_conf = {'bootstrap.servers': 'kafka:9092',
                         'client.id': socket.gethostname()}
        consumer_conf = {'bootstrap.servers': 'kafka:9092',
                         'group.id': 'sentiment-analysis_consumer',
                         'client.id': socket.gethostname()}
        self.__consumer__ = aiokafka.AIOKafkaConsumer(
            KAFKA_REQUEST_TOPIC,
            group_id='sentiment-analysis_consumer',
            bootstrap_servers='kafka:9092'
        )
        self.__producer__ = aiokafka.AIOKafkaProducer(
            bootstrap_servers='kafka:9092', client_id=socket.gethostname())
        # self.__producer__ = Producer(producer_conf)
        # self.produce_analysis(text="I love this movie and i would watch it again and again!", uuid=uuid.uuid4())

    async def __produce_analysis__(self, text: string, uuid: UUID):
        result = max(self.__classifier__(text)[0], key=lambda x: x['score'])
        byte_value = json.dumps(result).encode("utf-8")
        # byte_key = json.dumps(uuid, cls=UUIDEncoder)
        byte_key = str(uuid).encode("utf-8")
        try:
            await self.__producer__.send(topic=KAFKA_RESPONSE_TOPIC, key=byte_key, value=byte_value)
        except Exception as e:
            print(f"Error sending message: {e}")

    async def consume(self):
        await self.__consumer__.start()
        await self.__producer__.start()
        try:
            async for msg in self.__consumer__:
                text = msg.value.decode('utf-8')
                uuid = UUID(msg.key.decode('utf-8'))
                await self.__produce_analysis__(text, uuid)
        finally:
            await self.__consumer__.stop()
            await self.__producer__.stop()
