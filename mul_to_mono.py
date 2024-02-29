# convert multi channel audio to mono channel audio

from pydub import AudioSegment

# Load the stereo audio
audio = AudioSegment.from_wav('audio.wav')

# Convert to mono audio
mono_audio = audio.set_channels(1)

# Export the mono audio to a new WAV file
mono_audio.export('mono_audio.wav', format='wav')