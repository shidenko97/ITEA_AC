import asyncio


async def compute(x, y):
    print("Compute %s + %s ..." % (x, y))
    await asyncio.sleep(5.0)
    return x + y

async def compute_2(x, y):
    print("Compute %s + %s ..." % (x, y))
    return x + y


async def print_sum(x, y):
    result_1 = asyncio.ensure_future(compute(x, y))
    result_2 = asyncio.ensure_future(compute_2(x, y))
    res_2 = await result_2
    res_1 = await result_1
    print()
    # print("%s + %s = %s" % (x, y, task))
    # print("%s + %s = %s" % (x, y, task_2))

loop = asyncio.get_event_loop()
loop.run_until_complete(print_sum(1, 2))
loop.close()
