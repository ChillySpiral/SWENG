import os
from transformers import pipeline

os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'


class SentimentAnalyser:
    def __init__(self, model="lxyuan/distilbert-base-multilingual-cased-sentiments-student"):
        self.__classifier__ = pipeline(
            model=model,
            top_k=None
        )

    def get_analysis(self, text):
        print(self.__classifier__(text))
