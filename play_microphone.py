# Play with audio data from microphone
# %%
import speech_recognition as sr

# %%
r = sr.Recognizer()
mic = sr.Microphone()

# %% List microphone names
sr.Microphone.list_microphone_names()


# %%
mic = sr.Microphone(device_index=1)


# %%
with mic as source:
    audio = r.listen(source)


# %%
r.recognize_google(audio)


# %%
