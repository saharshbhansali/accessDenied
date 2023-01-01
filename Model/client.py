import asyncio

# This is the main function of the client
async def main():
    # Connect to the server
    reader, writer = await asyncio.open_connection('127.0.0.1', 8888)

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

await main()
