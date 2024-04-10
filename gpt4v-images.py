# https://cookbook.openai.com/examples/gpt_with_vision_for_video_understanding

# dotenv
import os
from dotenv import load_dotenv

load_dotenv()

HUME_API_KEY = os.getenv("HUME_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

print("HUME_API_KEY=", HUME_API_KEY)
print("OPENAI_API_KEY=", OPENAI_API_KEY)

# OpenAI API Key
from openai import OpenAI

client = OpenAI(api_key=OPENAI_API_KEY)

"""
Input url images
https://platform.openai.com/docs/guides/vision/quick-start

output = Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='This image features a wooden boardwalk path extending through a lush green wetland or meadow under a partly cloudy sky. The vegetation is dense and tall, consisting primarily of grasses, with scattered bushes and trees. The landscape is flat, and the sky is vivid with blue hues and wispy clouds. The scene conveys a sense of tranquility and the natural beauty of a protected ecological area, likely designed for walking and enjoying nature without disturbing the habitat.', role='assistant', function_call=None, tool_calls=None))
"""

response = client.chat.completions.create(
    model="gpt-4-turbo",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "What’s in this image?"},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
                    },
                },
            ],
        }
    ],
    max_tokens=300,
)

print(response.choices[0])

"""
Input local base64 images
https://platform.openai.com/docs/guides/vision/uploading-base-64-encoded-images

output = {'id': 'chatcmpl-9CD4UHUXcvJ1te1tLie8URg0V0hNw', 'object': 'chat.completion', 'created': 1712697210, 'model': 'gpt-4-turbo-2024-04-09', 'choices': [{'index': 0, 'message': {'role': 'assistant', 'content': 'The image features a portrait of a man from a historical era, likely from the 17th or 18th century, based on his attire. He is wearing a decorated coat with ornate patterns and a wig, typical of European aristocratic fashion of the time. His expression is mild and formal, fitting the portrait style of that period. The image is in black and white, suggesting it might be an engraving or a print.'}, 'logprobs': None, 'finish_reason': 'stop'}], 'usage': {'prompt_tokens': 268, 'completion_tokens': 88, 'total_tokens': 356}, 'system_fingerprint': 'fp_c6d3ee77af'}

"""
# https://platform.openai.com/docs/guides/vision/uploading-base-64-encoded-images
import base64
import requests


# Function to encode the image
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


# Path to your image
image_path = "david_hume.jpeg"

# Getting the base64 string
base64_image = encode_image(image_path)

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {OPENAI_API_KEY}",
}

payload = {
    "model": "gpt-4-turbo",
    "messages": [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "What’s in this image?"},
                {
                    "type": "image_url",
                    "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"},
                },
            ],
        }
    ],
    "max_tokens": 300,
}

response = requests.post(
    "https://api.openai.com/v1/chat/completions", headers=headers, json=payload
)

print(response.json())


"""
Multiple image inputs
https://platform.openai.com/docs/guides/vision/multiple-image-inputs

output = Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content="The images you've posted appear to be identical. Each image shows a scenic landscape featuring a wooden boardwalk leading through a lush, green wetland or grassy area under a partly cloudy blue sky. The boardwalk serves as a pathway through the nature area, likely intended to protect the environment and provide visitors a route to enjoy the surroundings without disturbing the natural habitat. The images capture a vibrant ecosystem that includes various green vegetation under a beautiful sky, contributing to a serene and natural atmosphere.", role='assistant', function_call=None, tool_calls=None))

"""
response = client.chat.completions.create(
    model="gpt-4-turbo",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "What are in these images? Is there any difference between them?",
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
                    },
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
                    },
                },
            ],
        }
    ],
    max_tokens=300,
)
print(response.choices[0])


"""
Low or high fidelity image understanding
https://platform.openai.com/docs/guides/vision/low-or-high-fidelity-image-understanding

"""

from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4-turbo",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "What’s in this image?"},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
                        "detail": "high",
                    },
                },
            ],
        }
    ],
    max_tokens=300,
)

print(response.choices[0].message.content)
