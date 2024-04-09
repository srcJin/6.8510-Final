from hume import HumeBatchClient
from hume.models.config import FaceConfig

client = HumeBatchClient("Vz2nqOA7FOxeC6sFosfR3M9AIjX29i4aeJF6ytLfOYxrvAv4")
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
job.download_artifacts("filename.zip")
