import asyncio


async def async_main():
    t1 = asyncio.create_task(dance())
    t2 = asyncio.create_task(learn_and_sing())

    print("waiting to learn the song, sing it and daaance!")

    await t1
    print("done dancing")

    await t2


async def learn_and_sing():
    song = await learn_song()
    await sing_song(song)


async def learn_song():
    await asyncio.sleep(0.6)
    return "this is the song"


async def sing_song(song):
    print(song)


async def dance():
    for i in range(10):
        await asyncio.sleep(0.1)
        print(i)


if __name__ == "__main__":
    asyncio.run(async_main())
