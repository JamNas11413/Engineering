# asyncio, thread and processes





    # doing multiple stuff at once without waiting for the 1st one to be completeted


# asyncio:
    # for maninging mainy waoting tast  effiiciently(not much cpu usage)
# thread:
    # for parrel tats that share data with with minimal cpu usage 
# processes:
    # for maximizing performance on cpu intensive tasks that can be parrelled but dont share data


# asyncio:

# event-loop:
    # manage and distribute tasks

import asyncio

async def main():   # async func => coroutine func
    print("start of main coroutine!")

# asyncio.run(main())   # run the main coroutine and wait for it to complete # the asyncio.run() will start our event loop

# main()  # -> we are genrating a coroutine object but not running it yet, we need to await it or run it in the event loop to execute it
# i.e
# print(main()) # will give coroutine object
# when we call a func defined with async kw it returns a coroutine obj
# if we want the obj to be exe we have to await it


async def second():
    await main()
    print("End of main coroutine!")

asyncio.run(second())


