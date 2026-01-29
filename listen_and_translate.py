import asyncio
from bleak import BleakClient

from settings import TreadmillSettings


def parse_treadmill_packet(data: bytes):
    if len(data) != 19:
        return None

    speed_raw = data[2] | (data[3] << 8)
    incline_raw = data[7] | (data[8] << 8)

    return {
        "speed_kmh": speed_raw / 100.0,
        "incline_percent": incline_raw / 10.0,
        "state": data[11],
        "counter": data[18],
        "raw_hex": data.hex()
    }



async def handler(sender, data):
    parsed = parse_treadmill_packet(data)
    if parsed:
        print(
            f"Speed {parsed['speed_kmh']:.2f} km/h | "
            f"Incline {parsed['incline_percent']:.1f}% | "
            f"State {parsed['state']} | "
            f"Counter {parsed['counter']}"
        )

async def main():
    settings = TreadmillSettings()
    print("Connecting to:", settings.mac)
    async with BleakClient(settings.mac) as client:
        print("Connected")
        await client.start_notify(settings.char_uuid, handler)
        print("Notify enabled")

        while True:
            await asyncio.sleep(1)

asyncio.run(main())
