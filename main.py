import asyncio
from lagrange.client.base import BaseClient
from lagrange.info.app import app_list
from lagrange.info.device import DeviceInfo


async def main():
    client = BaseClient(114514, app_list['linux'], DeviceInfo.generate(114514))
    client.connect()
    await client.fetch_qrcode()
    await client.wait_closed()


if __name__ == '__main__':
    asyncio.run(main())
