import asyncio
from hume import HumeStreamClient, StreamSocket
from hume.models.config import LanguageConfig, FaceConfig, ProsodyConfig

samples = [
    "Mary had a little lamb,",
    "Its fleece was white as snow."
    "Everywhere the child went,"
    "The little lamb was sure to go.",
]


async def main():
    client = HumeStreamClient("Vz2nqOA7FOxeC6sFosfR3M9AIjX29i4aeJF6ytLfOYxrvAv4")
    config = LanguageConfig()
    async with client.connect([config]) as socket:
        for sample in samples:
            result = await socket.send_text(sample)
            emotions = result["language"]["predictions"][0]["emotions"]
            print(emotions)


asyncio.run(main())


async def main():
    client = HumeStreamClient("Vz2nqOA7FOxeC6sFosfR3M9AIjX29i4aeJF6ytLfOYxrvAv4")
    config = FaceConfig(identify_faces=True)

    async with client.connect([config]) as socket:
        result = await socket.send_file("david_hume.jpeg")
        print(result)


asyncio.run(main())


# async def main():
#     client = HumeStreamClient("Vz2nqOA7FOxeC6sFosfR3M9AIjX29i4aeJF6ytLfOYxrvAv4")
#     config = ProsodyConfig()
#     async with client.connect([config]) as socket:
#         result = await socket.send_file("<YOUR VIDEO OR AUDIO FILEPATH>")
#         print(result)


# asyncio.run(main())
