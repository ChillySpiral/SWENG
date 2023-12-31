import asyncio
import uuid

from ml_features.sentiment_analysis import SentimentAnalyser
from ml_features.text_generation import TextGenerator


async def main():
    sentiment_analyser = SentimentAnalyser()
    await sentiment_analyser.consume()


if __name__ == '__main__':
    asyncio.run(main())
