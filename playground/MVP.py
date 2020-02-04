# Play with wav audio file speech to text

# %%
import speech_recognition as sr
from os import path
sr.__version__
r = sr.Recognizer()

# analyze entire audio source
# %% Set directory & file
snippetDIR = '/Users/troy/APFM/ROOT_CO/Snippets'
snippet = snippetDIR + '/LID19575241_CID84488994_Ronald_Robinson_20200117.wav'
print(snippet)

# %% Process
# Call sr on autofile type "snippet"
processAudioFile = sr.AudioFile(snippet)

# Check file type
type(processAudioFile)

# %%

with processAudioFile as source:
    audio = r.record(source)
type(audio)
transcription = r.recognize_google(audio)
print(transcription)

# %%
# Function to save transcription string to a text file at x directory


def saveTranscriptionToFile(transcription):
    file = open(
        r"/Users/troy/APFM/ROOT_CO/Snippets/transcriptions/latest.txt", "w+")
    file.write(transcription)
    file.close()


# %% Analyze audio in snippets
test = processAudioFile  # reuse audiofile from before

with test as source:
    # measure of duration and offset in seconds
    audio1 = r.record(source, offset=0, duration=5)
    audio2 = r.record(source, offset=5, duration=5)
    audio3 = r.record(source, offset=10, duration=5)
    # audio4 = r.record(source, duration=40)
    # audio5 = r.record(source, duration=40)
    # audio6 = r.record(source, duration=40)
    # audio7 = r.record(source, duration=40)

print(r.recognize_google(audio1))
print(r.recognize_google(audio2))
print(r.recognize_google(audio3))
# print(r.recognize_google(audio4))
# print(r.recognize_google(audio5))
# print(r.recognize_google(audio6))
# print(r.recognize_google(audio7))

# %% Run transcription in Cloud

# - will return a dictionary to see possibilities
# resultFromCloud = r.recognize_google(audio1, show_all=True)
# - return just string
# resultFromCloud = r.recognize_google(audio1)  # return a string
# saveTranscriptionToFile(resultFromCloud)
# print(resultFromCloud)

for k, v in resultFromCloud.items():
    print(k, v)

# %%
