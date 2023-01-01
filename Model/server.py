import asyncio

async def main():
    reader, writer = await asyncio.open_connection('127.0.0.1', 8888)

    message = 'Hello, World!'
    print(f'Send: {message!r}')
    writer.write(message.encode())
    await writer.drain()

    data = await reader.read(100)
    print(f'Received: {data.decode()!r}')

    print('Close the connection')
    writer.close()

await main()
