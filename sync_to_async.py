import asyncio


async def sync_to_async(func):
    async def wrapper(*args, **kwargs):
        res = await asyncio.to_thread(func(*args, **kwargs))
        return res
    return wrapper
