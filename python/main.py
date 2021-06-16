import asyncio


async def async_main():
    # Will create hot tasks that starts executing immediately.
    t1 = asyncio.create_task(dance())
    t2 = asyncio.create_task(learn_and_sing())

    print("waiting to learn the song, sing it and daaance!")

    # We await both tasks to ensure their completion, however since we know that
    # t1 will always run longer than t2 it would be enough to await t1 to have
    # both executed until done. This is however somewhat more clear.
    await t1
    await t2

    print("done dancing")


async def async_main_gather():
    print("waiting to learn the song, sing it and daaance!")

    # An alternative way would be to just gather all the tasks and ensure
    # they're finished by blocking until all are done.
    await asyncio.gather(
        dance(),
        learn_and_sing(),
    )

    print("done dancing")


async def learn_and_sing():
    song = await learn_song()
    sing_song(song)


async def learn_song():
    await asyncio.sleep(0.6)
    return "this is the song"


def sing_song(song):
    print(song)


async def dance():
    for i in range(10):
        await asyncio.sleep(0.1)
        print(i)


if __name__ == "__main__":
    asyncio.run(async_main())
