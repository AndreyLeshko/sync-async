import asyncio


async def sync_to_async(func):
    async def wrapper(*args, **kwargs):
        res = await asyncio.to_thread(func(*args, **kwargs))
        return res

    return wrapper


def async_to_sync(func):
    def wrapper(*args, **kwargs):
        loop = asyncio.get_event_loop()
        if loop.is_running():
            message = ('You cannot synchronously execute an asynchronous function from a running event loop.' +
                       'Use await syntax to run runction')
            raise RuntimeError(message)
        else:
            res = loop.run_until_complete(func(*args, **kwargs))
        return res

    return wrapper
