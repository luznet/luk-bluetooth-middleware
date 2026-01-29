import asyncio
from bleak import BleakClient

TREADMILL_MAC = ""  # replace with your treadmill MAC

async def main():
    async with BleakClient(TREADMILL_MAC) as client:
        print("Connected")

        for service in client.services:
            print(f"[SERVICE] {service.uuid}")
            for char in service.characteristics:
                print(f"   [CHAR] {char.uuid} | {char.properties}")

asyncio.run(main())
