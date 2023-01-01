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

    # Send the data back to the client
    print(f"Send: {message!r}")
    writer.write(data)
    await writer.drain()

    # Close the connection to the client
    print("Close the client socket")
    writer.close()

# This is the main function of the server
async def main():
    # Create three servers with the `handle_echo` function as the handler
    # for incoming connections
    server1 = await asyncio.start_server(handle_echo, '127.0.0.1', 8888)
    server2 = await asyncio.start_server(handle_echo, '127.0.0.1', 8889)
    server3 = await asyncio.start_server(handle_echo, '127.0.0.1', 8890)

    # Get the addresses of the servers
    addr1 = server1.sockets[0].getsockname()
    addr2 = server2.sockets[0].getsockname()
    addr3 = server3.sockets[0].getsockname()
    print(f'Serving on {addr1}')
    print(f'Serving on {addr2}')
    print(f'Serving on {addr3}')

    # Run the servers indefinitely
    async with server1, server2, server3:
        await asyncio.gather(server1.serve_forever(), server2.serve_forever(), server3.serve_forever())

asyncio.run(main())
