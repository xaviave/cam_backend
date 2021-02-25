import asyncio, asyncssh, sys


async def run_client():
    async with asyncssh.connect(
        host="192.168.1.28", port=2222, username="pi", password="Moorea10"
    ) as conn:
        result = await conn.run("ls", check=True)
        print(result.stdout, end="")


try:
    asyncio.get_event_loop().run_until_complete(run_client())
except (OSError, asyncssh.Error) as exc:
    sys.exit("SSH connection failed: " + str(exc))
