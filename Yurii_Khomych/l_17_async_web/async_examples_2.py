import asyncio
import uvloop


def compute(x, y):
    print("Compute %s + %s ..." % (x, y))
    return x + y


async def compute_2(x, y):
    print("Compute %s + %s ..." % (x, y))
    await asyncio.sleep(1.0)
    return x + y


async def print_sum(x, y):
    result = compute(x, y)
    result_2 = await compute_2(x, y)
    print("%s + %s = %s" % (x, y, result))
    print("%s + %s = %s" % (x, y, result_2))


loop = asyncio.get_event_loop()
loop.run_until_complete(print_sum(1, 2))
loop.close()

# gino
# user = asyncio.create_task(
#     User.query.where(User.nickname == "daisy").gino.first()
# )
# user_1 = asyncio.create_task(
#     User.query.where(User.nickname == "daisy").gino.first()
# )
# asyncio.create_task(User.insert())
...
# await user
# await user_1
