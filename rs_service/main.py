import asyncio
import multiprocessing

from rs_features.resizer import Resizer


async def run_resizer():
    resizer_local = Resizer()
    await resizer_local.initialize()
    await resizer_local.consume()


def start_resizer():
    asyncio.run(run_resizer())


if __name__ == '__main__':
    resize_process = multiprocessing.Process(target=start_resizer)
    resize_process.start()
