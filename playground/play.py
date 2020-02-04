# Play with wav audio file speech to text

# %%
import speech_recognition as sr
sr.__version__
r = sr.Recognizer()

# analyze entire audio source
# %%
harvard = sr.AudioFile(
    'python-speech-recognition/audio_files/harvard.wav')

with harvard as source:
    audio = r.record(source)
type(audio)
r.recognize_google(audio)

# %% test
test = sr.AudioFile(
    'python-speech-recognition/audio_files/test.flac')

with test as source:
    audio = r.record(source)
type(audio)
r.recognize_google(audio)

# %% analyze audio is snippets
harvard = sr.AudioFile(
    "python-speech-recognition/audio_files/harvard.wav")

with harvard as source:
    audio1 = r.record(source, duration=4)
    audio2 = r.record(source, duration=4)
type(audio)
# two diff audio
print(r.recognize_google(audio1))
print(r.recognize_google(audio2))


# %%
