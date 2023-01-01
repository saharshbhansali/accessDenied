import asyncio
import sys

# This is the main function of the client
async def main(port):
    # Connect to the server
    reader, writer = await asyncio.open_connection('127.0.0.1', port)

    # Send a message to the server
    message = 'Hello, World! @ ' + str(port) + ' !'
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

async def run_client(ports):
    for port in ports:
        await main(port)

def main():
    start = int(sys.argv[1])
    end = int(sys.argv[2])
    ports = range(start, end + 1)
    print(f"Ports:\n\tstart: {start}, end: {end}")
    asyncio.run(run_client(i for i in ports))

if __name__ == '__main__':
    main()