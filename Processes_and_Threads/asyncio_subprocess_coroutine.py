import asyncio
import asyncio.subprocess

async def run_df():
    print('in run_df')
    
    buffer = bytearray()

    create = asyncio.create_subprocess_exec(
        'df', '-hl',
        stdout=asyncio.subprocess.PIPE,
    )
    print('launching process')
    proc = await create
    print('process started {}'.format(proc.pid))

    while True:
        line = await proc.stdout.readline()
        print('read {!r}'.format(line))
        if not line:
            print('no more output from command')
            break
        buffer.extend(line)

    print('waiting for process to complete')
    await proc.wait()

    return_code = proc.returncode
    print('return code {}'.format(return_code))
    if not return_code:
        results = bytes(buffer).decode()
    else:
        results = ""

    return (return_code, results)

event_loop = asyncio.get_event_loop()
try:
    return_code, results = event_loop.run_until_complete(
        run_df()
    )
finally:
    event_loop.close()

