import asyncio
import multiprocessing

from ml_features.sentiment_analysis import SentimentAnalyser
from ml_features.text_generation import TextGenerator


async def run_sentiment_analyser():
    sentiment_analyser = SentimentAnalyser()
    await sentiment_analyser.initialize()
    await sentiment_analyser.consume()


async def run_text_generator():
    text_generator = TextGenerator()
    await text_generator.initialize()
    await text_generator.consume()


def start_sentiment_analyser():
    asyncio.run(run_sentiment_analyser())


def start_text_generator():
    asyncio.run(run_text_generator())


if __name__ == '__main__':
    sentiment_analyser_process = multiprocessing.Process(target=start_sentiment_analyser)
    text_generator_process = multiprocessing.Process(target=start_text_generator)

    sentiment_analyser_process.start()
    text_generator_process.start()
