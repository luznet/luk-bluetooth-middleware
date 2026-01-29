import asyncio
from bleak import BleakClient


async def handler(sender, data):
    print(f"[NOTIFY] {sender}: {data.hex()}")
    

async def main():
    async with BleakClient(TREADMILL_MAC) as client:
        print("Connected")
        await client.start_notify(CHAR_UUID, handler)
        print("Listening for notifications...")
        while True:
            await asyncio.sleep(1)

asyncio.run(main())
