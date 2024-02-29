## Speech Applications

The Speech Applications repository hosts two robust applications: Text to Speech and Speech to Text. Leveraging the capabilities of Google Cloud services, these applications provide streamlined solutions for converting between text and speech formats. Additionally, the repository contains essential API keys, necessary for seamless integration with Google Cloud, and a utility script for audio preprocessing. With its user-friendly Streamlit interface and comprehensive functionality, Speech Applications simplifies the process of working with speech data.

![Speech Applications Logo](/Speech%20Applications.png)

## Speech Applications Overview


**Text to Speech Application**

The Text to Speech application allows users to input text and convert it into speech. Implemented using Streamlit, this application simplifies the process of synthesizing speech. It involves setting up Google Cloud credentials, taking user input, synthesizing speech based on the input text, and presenting the synthesized audio to the user.


**Speech to Text Application**

The Speech to Text application facilitates the transcription of uploaded audio files into text. Also built using Streamlit, this application streamlines the process of transcribing spoken language. It includes functionalities such as setting up Google Cloud Speech client, defining a function to transcribe audio files, allowing users to upload audio files, and presenting the transcription result to the user.


**Audio Preprocessing**

The project includes a Python script, `convert_to_mono.py`, for converting audio files to mono channels. This preprocessing step is essential for utilizing the Speech to Text application effectively. The script reads audio files, converts them to mono channels, and saves the modified audio files.

**API Keys**
The repository contains JSON files (`sa_speech_demo.json` and `sa_text_demo.json`) that store API keys necessary for authentication with Google Cloud services. These keys are utilized by the Text to Speech and Speech to Text applications to access the respective Google Cloud APIs.

