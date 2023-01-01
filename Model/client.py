import asyncio

# This function sends a message to a specific server
async def send_message(server_id, message):
    # Connect to the server
    reader, writer = await asyncio.open_connection('127.0.0.1', 8888 + server_id)

    # Send a message to the server
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

# This is the main function of the client
def run_clients():
    # Send a message to each of the three servers
    a1 = asyncio.run(send_message(0, 'Hello, Server 0!'))
    a2 = asyncio.run(send_message(1, 'Hello, Server 1!'))
    a3 = asyncio.run(send_message(2, 'Hello, Server 2!'))
    asyncio.run(asyncio.gather(a1, a2, a3))
    # await asyncio.gather(send_message(0, 'Hello, Server 0!'), send_message(1, 'Hello, Server 1!'), send_message(2, 'Hello, Server 2!'))

run_clients()