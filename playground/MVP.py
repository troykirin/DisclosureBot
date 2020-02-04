# Play with wav audio file speech to text

# %%
import speech_recognition as sr
sr.__version__
r = sr.Recognizer()

# analyze entire audio source
# %% test
test = sr.AudioFile(
    'python-speech-recognition/audio_files/test.wav')

with test as source:
    audio = r.record(source)
type(audio)
transcription = r.recognize_google(audio)
print(transcription)

# save to a text file
file = open(r"python-speech-recognition/audio_files/text.txt", "w+")
test = 'test'
file.write(test)
file.close()

# %% analyze audio in snippets
test = sr.AudioFile(
    "python-speech-recognition/audio_files/test.wav")

with test as source:
    audio1 = r.record(source, duration=40)
    audio2 = r.record(source, duration=40)
    # audio3 = r.record(source, duration=40)
    # audio4 = r.record(source, duration=40)
    # audio5 = r.record(source, duration=40)
    # audio6 = r.record(source, duration=40)
    # audio7 = r.record(source, duration=40)

type(audio)
# two diff audio
print(r.recognize_google(audio1))
print(r.recognize_google(audio2))
# print(r.recognize_google(audio3))
# print(r.recognize_google(audio4))
# print(r.recognize_google(audio5))
# print(r.recognize_google(audio6))
# print(r.recognize_google(audio7))

# %%