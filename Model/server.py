import asyncio

# This function is called whenever a new client connects to the server
async def handle_echo(reader, writer):
    # Read data from the client
    data = await reader.read(100)

    # Decode the data received from the client
    message = data.decode()

    # Get the address of the client
    addr = writer.get_extra_info('peername')

    # Print a message indicating that we received data from the client
    print(f"Received {message!r} from {addr!r}")

    # Send the data to all connected clients
    for client in clients:
        client.write(data)
        await client.drain()

    # Close the connection to the client
    print("Close the client socket")
    writer.close()

# This is the main function of the server
async def main():
    # Create a server with the `handle_echo` function as the handler
    # for incoming connections
    server = await asyncio.start_server(handle_echo, '127.0.0.1', 8888)

    # Get the address of the server
    addr = server.sockets[0].getsockname()
    print(f'Serving on {addr}')

    # Add the server to the list of clients
    clients.append(server)

    # Run the server indefinitely
    async with server:
        await server.serve_forever()

# Create an empty list to store connected clients
clients = []

# Run the main function in an asyncio event loop
asyncio.run(main())
