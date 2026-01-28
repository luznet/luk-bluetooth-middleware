import asyncio
from bleak import BleakScanner, BleakClient

# Replace with your treadmill's BLE service/characteristic UUIDs
SERVICE_UUID = "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
CHAR_UUID = "yyyyyyyy-yyyy-yyyy-yyyy-yyyyyyyyyyyy"

async def notification_handler(sender, data):
    """
    Called whenever the treadmill sends BLE data.
    'data' will be bytes; you can decode or parse it.
    """
    print(f"[BLE] Notification from {sender}: {data}")

async def main():
    print("Scanning for BLE devices...")
    devices = await BleakScanner.discover()

    for d in devices:
        print(f"Found: {d.name} - {d.address}")

    # You will need to identify your treadmill's MAC address manually
    treadmill_mac = "AA:BB:CC:DD:EE:FF"

    print(f"Connecting to {treadmill_mac}...")
    async with BleakClient(treadmill_mac) as client:
        print("Connected.")

        # Subscribe to treadmill notifications
        await client.start_notify(CHAR_UUID, notification_handler)

        print("Listening for BLE notifications...")
        while True:
            await asyncio.sleep(1)

asyncio.run(main())
