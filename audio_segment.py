from pydub import AudioSegment
import math

# Define the path to the uploaded MP3 file and the segment length in milliseconds (15000ms = 15s)
file_path = "audio.mp3"
segment_length = 15000

# Load the audio file
audio = AudioSegment.from_mp3(file_path)

# Calculate the number of segments
duration = len(audio)
num_segments = math.ceil(duration / segment_length)

# Split the audio and save the segments
segments_paths = []
for i in range(num_segments):
    start = i * segment_length
    end = start + segment_length
    segment = audio[start:end]

    # Save segment to file
    segment_path = f"/output/segment_{i+1}.mp3"
    segment.export(segment_path, format="mp3")
    segments_paths.append(segment_path)

segments_paths
