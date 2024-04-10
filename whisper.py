# https://platform.openai.com/docs/guides/speech-to-text/longer-inputs

from openai import OpenAI

OPENAI_API_KEY = "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"

client = OpenAI(api_key=OPENAI_API_KEY)


"""
whisper audio to text
output= By the time they arrived at the courthouse in Hackensack, it was nearly 10 p.m. Big Cindy sat in the rain, shoulders hunched. Myron stepped out of the car and approached. Big Cindy?
"""

audio_file = open("segment_1.mp3", "rb")
transcription = client.audio.transcriptions.create(
    model="whisper-1", file=audio_file, response_format="text"
)
print(transcription)


"""
whisper audio to text, with timestamps

output= [{'word': 'By', 'start': 0.0, 'end': 0.3199999928474426}, {'word': 'the', 'start': 0.3199999928474426, 'end': 0.46000000834465027}, {'word': 'time', 'start': 0.46000000834465027, 'end': 0.7200000286102295}, {'word': 'they', 'start': 0.7200000286102295, 'end': 0.9200000166893005}]

"""

transcript = client.audio.transcriptions.create(
    file=audio_file,
    model="whisper-1",
    response_format="verbose_json",
    timestamp_granularities=["word"],
)

print(transcript.words)


"""
prompting
Whisper only considers the first 244 tokens of the prompt
"""

transcription = client.audio.transcriptions.create(
    model="whisper-1",
    file=audio_file,
    response_format="text",
    prompt="ZyntriQix, Digique Plus, CynapseFive, VortiQore V8, EchoNix Array, OrbitalLink Seven, DigiFractal Matrix, PULSE, RAPT, B.R.I.C.K., Q.U.A.R.T.Z., F.L.I.N.T.",
)
print(transcription)


"""
post processing the transcriptions using GPT-4
"""

system_prompt = "You are a helpful assistant for the company ZyntriQix. Your task is to correct any spelling discrepancies in the transcribed text. Make sure that the names of the following products are spelled correctly: ZyntriQix, Digique Plus, CynapseFive, VortiQore V8, EchoNix Array, OrbitalLink Seven, DigiFractal Matrix, PULSE, RAPT, B.R.I.C.K., Q.U.A.R.T.Z., F.L.I.N.T. Only add necessary punctuation such as periods, commas, and capitalization, and use only the context provided."


def generate_corrected_transcript(temperature, system_prompt, audio_file):
    response = client.chat.completions.create(
        model="gpt-4-turbo-preview",
        temperature=temperature,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": transcribe(audio_file, "")},
        ],
    )
    return completion.choices[0].message.content


corrected_text = generate_corrected_transcript(0, system_prompt, "output/output.txt")


"""
segment longer inputs before processing

"""

from pydub import AudioSegment


def segmentAudio(audio):

    song = AudioSegment.from_mp3("good_morning.mp3")

    # PyDub handles time in milliseconds
    ten_minutes = 10 * 60 * 1000

    first_10_minutes = song[:ten_minutes]

    first_10_minutes.export("good_morning_10.mp3", format="mp3")

    return None
