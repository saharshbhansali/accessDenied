import asyncio

# This function is called whenever a new client connects to the server
async def handle_echo(reader, writer):
    while True:
        # Read data from the client
        data = await reader.read(100)
        if not data:
            break

        # Decode the data received from the client
        message = data.decode()

        # Get the address of the client
        addr = writer.get_extra_info('peername')

        # Print a message indicating that we received data from the client
        print(f"Received {message!r} from {addr!r}")

        # Send the data back to the client
        print(f"Send: {message!r}")
        writer.write(data)
        await writer.drain()

    # Close the connection to the client
    print("Close the client socket")
    writer.close()

# This is the main function of the server
async def main(port):
    # Create a server with the `handle_echo` function as the handler
    # for incoming connections
    server = await asyncio.start_server(handle_echo, '127.0.0.1', port)

    # Get the address of the server
    addr = server.sockets[0].getsockname()
    print(f'Serving on {addr}')

    # Run the server indefinitely
    async with server:
        await server.serve_forever()

    # Start three servers on different ports
    server1 = asyncio.create_task(main(8888))
    server2 = asyncio.create_task(main(8889))
    server3 = asyncio.create_task(main(8890))

    # Wait for the servers to finish
    await asyncio.gather(server1, server2, server3)

asyncio.run(main(8888))