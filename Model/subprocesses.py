import asyncio

async def run_subprocess_v1(port):
    # Start the subprocess
    process = await asyncio.create_subprocess_exec('python', 'server.py', port, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)

    # Wait for the subprocess to complete
    stdout, stderr = await process.communicate()

    # Print the output of the subprocess
    print(f'Subprocess exited with exit code {process.returncode}')
    print(f'Standard output: {stdout.decode()}')
    print(f'Standard error: {stderr.decode()}')

async def run_subprocess_v2(port):
    # Start the subprocess
    process = await asyncio.create_subprocess_exec('python', 'myscript.py', args=[port], stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)

    # Wait for the subprocess to complete
    await process.wait()

    # Print the exit code of the subprocess
    print(f'Subprocess exited with exit code {process.returncode}')


asyncio.run(run_subprocess_v1('8888'))
asyncio.run(run_subprocess_v1('8889'))
asyncio.run(run_subprocess_v1('8890'))

# asyncio.run(run_subprocess_v2('8888'))
# asyncio.run(run_subprocess_v2('8889'))
# asyncio.run(run_subprocess_v2('8890'))
