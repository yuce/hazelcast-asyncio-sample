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
    client = await HazelcastClient.create_and_start()
    print("get or create the map proxy")
    m = await client.get_map("amap")
    print("operate on the map")
    await map_op(m)

if __name__ == "__main__":
    asyncio.run(amain())

