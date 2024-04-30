"""
hume: Processing batches of media files
https://dev.hume.ai/docs/expression-measurement-api/rest
"""

from hume import HumeBatchClient
from hume.models.config import FaceConfig

import os
from dotenv import load_dotenv

load_dotenv()

HUME_API_KEY = os.getenv("HUME_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

print("HUME_API_KEY=", HUME_API_KEY)
print("OPENAI_API_KEY=", OPENAI_API_KEY)


client = HumeBatchClient(HUME_API_KEY)
filepaths = [
    "faces.zip",
    "david_hume.jpeg",
]
config = FaceConfig()
job = client.submit_job(None, [config], files=filepaths)
print(job)
print("Running...")
details = job.await_complete()
job.download_predictions("predictions.json")
print("Predictions downloaded to predictions.json")

# To get predictions as JSON use the Get job predictions endpoint.
job.get_predictions()
job.download_predictions("filename.json")

# To get predictions as a compressed file of CSVs, one per model use the Get job artifacts endpoint.
# job.download_artifacts("filename.zip")


"""
output format:
"""

output = [
    {
        "source": {
            "type": "file",
            "filename": "david_hume.jpeg",
            "content_type": None,  # Use None for null values in Python
            "md5sum": "85a49dcc4807a9032e1aaec4046f82da",
        },
        "results": {
            "predictions": [
                {
                    "file": "david_hume.jpeg",
                    "file_type": "image",
                    "models": {
                        "face": {
                            "metadata": None,
                            "grouped_predictions": [
                                {
                                    "id": "unknown",
                                    "predictions": [
                                        {
                                            "frame": 0,
                                            "time": 0.0,
                                            "prob": 0.9999545812606812,
                                            "box": {
                                                "x": 94.03748321533203,
                                                "y": 38.410621643066406,
                                                "w": 66.27411651611328,
                                                "h": 86.32630920410156,
                                            },
                                            "emotions": [
                                                {
                                                    "name": "Admiration",
                                                    "score": 0.16304227709770203,
                                                },
                                                {
                                                    "name": "Adoration",
                                                    "score": 0.1367497444152832,
                                                },
                                                {
                                                    "name": "Aesthetic Appreciation",
                                                    "score": 0.10224184393882751,
                                                },
                                                {
                                                    "name": "Amusement",
                                                    "score": 0.2809807360172272,
                                                },
                                                {
                                                    "name": "Anger",
                                                    "score": 0.05374865606427193,
                                                },
                                                {
                                                    "name": "Anxiety",
                                                    "score": 0.10858460515737534,
                                                },
                                            ],
                                        }
                                    ],
                                }
                            ],
                        }
                    },
                }
            ]
        },
    }
]
