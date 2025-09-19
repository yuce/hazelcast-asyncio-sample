import asyncio
import logging
import time


from hazelcast.asyncio import HazelcastClient
from hazelcast.asyncio import Map

logging.basicConfig(level=logging.DEBUG)


async def map_op(m: Map):
    print(m)
    key1 = str(time.time())
    await m.set(key1, "bar")
    v = await m.get(key1)
    print("V:", v)


async def amain():
    print("create the client")
    client = HazelcastClient()
    print("starting the client...")
    await client._start()

    m = await client.get_map("amap")
    await map_op(m)

if __name__ == "__main__":
    asyncio.run(amain())

