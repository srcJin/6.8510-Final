"""
Real-time measurement streaming

https://dev.hume.ai/docs/expression-measurement-api/websocket

pip install "hume[stream]"
"""

import asyncio
from hume import HumeStreamClient, StreamSocket
from hume.models.config import LanguageConfig, FaceConfig, ProsodyConfig


import os
from dotenv import load_dotenv

load_dotenv()

HUME_API_KEY = os.getenv("HUME_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

print("HUME_API_KEY=", HUME_API_KEY)
print("OPENAI_API_KEY=", OPENAI_API_KEY)

"""
Emotional language from text
"""
samples = [
    "Mary had a little lamb,",
    "Its fleece was white as snow."
    "Everywhere the child went,"
    "The little lamb was sure to go.",
]


async def main():
    client = HumeStreamClient(HUME_API_KEY)
    config = LanguageConfig()
    async with client.connect([config]) as socket:
        for sample in samples:
            result = await socket.send_text(sample)
            emotions = result["language"]["predictions"][0]["emotions"]
            print(emotions)


asyncio.run(main())


"""
Facial expressions from an image
"""


async def main():
    client = HumeStreamClient(HUME_API_KEY)
    config = FaceConfig(identify_faces=True)

    async with client.connect([config]) as socket:
        result = await socket.send_file("david_hume.jpeg")
        print(result)


asyncio.run(main())

"""
Speech prosody from an audio or video file
"""


# async def main():
#     client = HumeStreamClient("Vz2nqOA7FOxeC6sFosfR3M9AIjX29i4aeJF6ytLfOYxrvAv4")
#     config = ProsodyConfig()
#     async with client.connect([config]) as socket:
#         result = await socket.send_file("<YOUR VIDEO OR AUDIO FILEPATH>")
#         print(result)


# asyncio.run(main())
