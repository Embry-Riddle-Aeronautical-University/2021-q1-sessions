import asyncio
import random


async def produce(q, n):
    for x in range(1, n + 1):
        print(f'producing {x}/{n}')
        await asyncio.sleep(random.random())  # producing an item may take some time ...
        await q.put(str(x))  # put the item in the queue
    await q.put(None)  # indicate the producer is done


async def consume(q):
    while True:
        item = await q.get()  # wait for an item from the producer
        if item is not None:
            print(f'consuming item {item}')
            await asyncio.sleep(random.random())  # consuming an item may take some time ...
        else:
            # the producer emits None to indicate that it is done
            break


loop = asyncio.get_event_loop()
queue = asyncio.Queue()
producer = produce(queue, 10)
consumer = consume(queue)
loop.run_until_complete(asyncio.gather(producer, consumer))
loop.close()
