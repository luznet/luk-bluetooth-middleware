import asyncio
from bleak import BleakScanner

async def main():
    print("Scanning for BLE devices...")
    devices = await BleakScanner.discover()

    for d in devices:
        print(f"{d.name}  |  {d.address}")

asyncio.run(main())
