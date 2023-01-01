import asyncio

async def main(port):
    # Connect to the server
    reader, writer = await asyncio.open_connection('127.0.0.1', port)

    # Send a message to the server
    message = 'Hello, World!'
    print(f'Send: {message!r}')
    writer.write(message.encode())
    await writer.drain()

    # Wait for a response from the server
    data = await reader.read(100)

    # Print the response from the server
    print(f'Received: {data.decode()!r}')

    # Close the connection
    print('Close the connection')
    writer.close()

    # Connect to each server
    client1 = asyncio.create_task(main(8888))
    client2 = asyncio.create_task(main(8889))
    client3 = asyncio.create_task(main(8890))

    # Wait for the clients to finish
    await asyncio.gather(client1, client2, client3)

asyncio.run(main(8888))
