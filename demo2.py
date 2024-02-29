import os
from google.cloud import texttospeech_v1
from google.cloud import texttospeech


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'sa_text_demo.json'


client = texttospeech_v1.TextToSpeechClient()

text = '''
Grok is an AI modeled after the Hitchhiker’s Guide to the Galaxy, 
so intended to answer almost anything and, far harder, 
even suggest what questions to ask!

Grok is designed to answer questions with a bit of wit and has a rebellious streak, 
so please don’t use it if you hate humor!
'''

synthesis_input = texttospeech_v1.SynthesisInput(text = text)

# Configuring Voice
voice1 = texttospeech_v1.VoiceSelectionParams(
    language_code='en-US', 
    ssml_gender=texttospeech_v1.SsmlVoiceGender.MALE
)

# try asian accents and nigerian accents

# Configuring output file
audio_config = texttospeech_v1.AudioConfig(
    audio_encoding = texttospeech_v1.AudioEncoding.MP3
)

response = client.synthesize_speech(
    input=synthesis_input,
    voice=voice1,
    audio_config=audio_config
)

with open('audio file.wav', 'wb') as output1:
    output1.write(response.audio_content)