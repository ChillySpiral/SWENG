import os
import socket
import string
import json
import uuid
from uuid import UUID
from transformers import pipeline
from confluent_kafka import Producer
from dotenv import load_dotenv
from uuid_encoder import UUIDEncoder

os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

load_dotenv()
KAFKA_TOPIC = os.getenv('KAFKA_SENTIMENT_ANALYSIS_RESPONSE')


class SentimentAnalyser:
    def __init__(self, model="lxyuan/distilbert-base-multilingual-cased-sentiments-student"):
        self.__classifier__ = pipeline(
            model=model,
            top_k=None
        )
        conf = {'bootstrap.servers': 'kafka:9092',
                'client.id': socket.gethostname()}
        self.__producer__ = Producer(conf)
        self.produce_analysis(text="I love this movie and i would watch it again and again!", uuid=uuid.uuid4())

    def produce_analysis(self, text: string, uuid: UUID):
        result = max(self.__classifier__(text)[0], key=lambda x: x['score'])
        print(result)
        byte_value = json.dumps(result).encode("utf-8")
        byte_key = json.dumps(uuid, cls=UUIDEncoder)
        self.__producer__.produce(KAFKA_TOPIC, key=byte_key, value=byte_value)
