# STREAMLIT VERSION OF SPEECH-TO-TEXT APPLICATION

import streamlit as st
import io
from google.oauth2 import service_account
from google.cloud import speech

# Set up the Google Cloud Speech client
client_file = # Add the API key here
credentials = service_account.Credentials.from_service_account_file(client_file)
client = speech.SpeechClient(credentials=credentials)

# Define a function to transcribe an audio file
def transcribe_audio(audio_file_path):
    with io.open(audio_file_path, 'rb') as f:
        content = f.read()
        audio = speech.RecognitionAudio(content=content)

    config = speech.RecognitionConfig(
        encoding = speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz = 24000,
        language_code = "en-US",
        model = 'video'
    )

    response = client.recognize(config=config, audio=audio)

    transcript = ''
    for result in response.results:
        transcript += result.alternatives[0].transcript

    return transcript

# Initialize Streamlit app
st.title("Speech to Text App")

# Allow the user to upload an audio file
uploaded_file = st.file_uploader('Upload an audio file to be transcribed')

# Transcribe the audio file if the user has uploaded one
if uploaded_file is not None:
    # Convert the UploadedFile object to a file path
    uploaded_file_path = uploaded_file.name

    # Transcribe the audio file from the temporary file
    transcription = transcribe_audio(uploaded_file_path)

    # Display the transcription to the user
    st.write('Transcription:')
    st.write(transcription)
