#!/usr/bin/env python

# Copyright 2017 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Language code : https://support.google.com/googleplay/android-developer/table/4419860?hl=en
#


"""Google Cloud Speech API sample that demonstrates word time offsets with language change option.
Example usage:
    python transcribe_word_time_offsets.py -s <language> resources/audio.raw
    python transcribe_word_time_offsets.py -s <language> \gs://cloud-samples-tests/speech/vr.flac
"""
# %%
import argparse
import io
import csv
import os
import errno


from google.oauth2 import service_account


credentials = service_account.Credentials.from_service_account_file(
    '/Users/troy/APFM-dev/gcp-transcribe-api-key.json')


def transcribe_file_with_word_time_offsets(speech_file, language='en-US'):
    """Transcribe the given audio file synchronously and output the word time
    offsets."""
    print("Start")

    # - STABLE BUILD -
    # from google.cloud import speech
    # from google.cloud.speech import enums
    # from google.cloud.speech import types

    # - BETA Build -
    from google.cloud import speech_v1p1beta1
    from google.cloud.speech_v1p1beta1 import enums
    from google.cloud.speech import types

    print("checking credentials")

    # client = speech.SpeechClient(credentials=credentials) # Stable
    client = speech_v1p1beta1.SpeechClient(credentials=credentials)  # BETA

    print("Checked")
    with io.open(speech_file, 'rb') as audio_file:
        content = audio_file.read()

    print("audio file read")

    audio = types.RecognitionAudio(content=content)

    print("config start")
    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
        language_code=language,
        enable_word_time_offsets=True,
        model=phone_call)

    print("Recognizing:")
    response = client.recognize(config, audio)
    print("Recognized")

    for result in response.results:
        alternative = result.alternatives[0]
        print('Transcript: {}'.format(alternative.transcript))

        for word_info in alternative.words:
            word = word_info.word
            start_time = word_info.start_time
            end_time = word_info.end_time
            print('Word: {}, start_time: {}, end_time: {}'.format(
                word,
                start_time.seconds + start_time.nanos * 1e-9,
                end_time.seconds + end_time.nanos * 1e-9))


# [START def_transcribe_gcs]
def transcribe_gcs_with_word_time_offsets(gcs_uri="gcs://generic", language='en-US'):
    """Transcribe the given audio file asynchronously and output the word time offsets."""

    # - STABLE BUILD -

    # from google.cloud import speech
    # from google.cloud.speech import enums
    # from google.cloud.speech import types

    # - BETA BUILD -
    from google.cloud import speech_v1p1beta1
    from google.cloud.speech_v1p1beta1 import enums
    from google.cloud.speech_v1p1beta1 import types

    # Default language to use
    language = 'en-US'

    # Ask user for gcs_uri
    gcs_uri = input("Please enter gcs_uri: ")
    # Print to confirm
    print("You just entered: ", gcs_uri)

    # client = speech.SpeechClient()  # STABLE
    client = speech_v1p1beta1.SpeechClient(credentials=credentials)  # BETA

    # list of phrases to use in boost
    phrases = []

    with open('/Users/troy/APFM-dev/transcribe/gcp_speech2text/disclosure_phrases.csv', 'r') as f:
        reader = csv.reader(f)
        disclosure_phrase_list = list(reader)

    # flatten_list
    flat_list = [
        item for sublist in disclosure_phrase_list for item in sublist]

    # Check flattened list
    # print(flat_list)

    disclosure_phrase_list = flat_list

    # to confirm
    print(disclosure_phrase_list)
    # [['This is the first line', 'Line1'],
    #  ['This is the second line', 'Line2'],
    #  ['This is the third line', 'Line3']]

    boost = 20.0  # how much to boost by
    speech_contexts_element = {"phrases": phrases,
                               "boost": boost}  # boost in a dictionary
    speech_contexts = [speech_contexts_element]

    enable_speaker_diarization = True
    diarization_speaker_count = 2

    audio = types.RecognitionAudio(uri=gcs_uri)

    # Form 1
    config = {
        "encoding": enums.RecognitionConfig.AudioEncoding.LINEAR16,
        "sample_rate_hertz": 8000,
        "language_code": 'en-US',
        "enable_word_time_offsets": True,
        "speech_contexts": speech_contexts,
        "model": "phone_call",
        "enable_speaker_diarization": enable_speaker_diarization,
        "diarization_speaker_count": diarization_speaker_count,

    }

    # Alt form
    # config = types.RecognitionConfig(
    #     encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
    #     sample_rate_hertz=8000,
    #     language_code=language,
    #     enable_word_time_offsets=True,
    # )

    operation = client.long_running_recognize(config, audio)

    print('Waiting for operation to complete...')
    result = operation.result(timeout=90)

    # String manipulate for only the LID & CID from gci
    # LID = gcs_uri[14:37]
    LID = gcs_uri[14:-4]
    print(LID)

    pathDir = "/Users/troy/APFM-dev/transcribe/gcp_speech2text/02-13/"

    transcript_filename = pathDir + LID + "_transcript.txt"
    os.makedirs(os.path.dirname(transcript_filename), exist_ok=True)

    with open(transcript_filename, "w") as f:
        f.write("Below is transcript: for {}\n".format(gcs_uri))

    # Print to Files
    # transcript_file_name = path+LID + "_transcript.txt"
    # print(transcript_file_name)
    # transcript_file = open(transcript_file_name, "x")  # create file
    # transcript_file = open(transcript_file_name, "w")  # write to file
    transcript_file = open(transcript_filename, "w")  # write to file
    transcript_file.write("Below is transcript: for {}\n".format(gcs_uri))

    timeLog_filename = pathDir + LID + "_timeLogs.txt"
    os.makedirs(os.path.dirname(timeLog_filename), exist_ok=True)

    with open(timeLog_filename, "a") as f:
        f.write("Below is time_logs: for {}\n".format(gcs_uri))

    # time_log_file_name = path+LID + "_time_log.txt"
    # time_log_file = open(time_log_file_name, "x")
    timeLog_file = open(timeLog_filename, "w")
    timeLog_file.write("Below is Time Logs: \n")
    timeLog_file = open(timeLog_filename, "a")

    # -- SPEAKER FILE --
    speaker_filename = pathDir + LID + "_speakers.txt"
    os.makedirs(os.path.dirname(speaker_filename), exist_ok=True)
    with open(timeLog_filename, "a") as f:
        f.write("Below is time_logs: for {}\n".format(gcs_uri))

    speaker_file = open(speaker_filename, "w")
    speaker_file.write("Below is Transcript with Speaker tags: \n")
    speaker_file = open(speaker_filename, "a")

    for result in result.results:
        alternative = result.alternatives[0]

        print('Transcript: {} \n'.format(alternative.transcript))
        transcript_file.write(
            'Transcript: {} \n'.format(alternative.transcript))

        print('Confidence: {} \n'.format(alternative.confidence))
        transcript_file.write(
            'Confidence Score: {} \n'.format(alternative.confidence))

        for word in alternative.words:
            print(u"Word: {}".format(word.word))
            speaker_file.write(u"Word: {}\n".format(word.word))
            print(u"Speaker tag: {}".format(word.speaker_tag))
            speaker_file.write(u"Speaker tag: {}\n".format(word.speaker_tag))

        for word_info in alternative.words:
            word = word_info.word
            start_time = word_info.start_time
            end_time = word_info.end_time

            timeLog_file.write('Word: {}, start_time: {},end_time: {} \n'.
                               format(
                                   word,
                                   start_time.seconds +
                                   start_time.nanos * 1e-9,
                                   end_time.seconds + end_time.nanos * 1e-9))

            print('Word: {}, start_time: {}, end_time: {}'.format(
                word,
                start_time.seconds + start_time.nanos * 1e-9,
                end_time.seconds + end_time.nanos * 1e-9))

    transcript_file.close()
    timeLog_file.close()
    speaker_file.close()

    # [END def_transcribe_gcs]


# %%
if __name__ == '__main__':
    # parser = argparse.ArgumentParser(description=__doc__,
    #                                  formatter_class=argparse.RawDescriptionHelpFormatter)
    # parser.add_argument(
    #     dest='path', help='File or GCS path for audio file to be recognized')
    # parser.add_argument("-s", "--string", type=str, required=True)
    # args = parser.parse_args()
    # if args.path.startswith('gs://'):
    #     transcribe_gcs_with_word_time_offsets(args.path, args.string)
    # else:
    #     transcribe_file_with_word_time_offsets(args.path, args.string)
    transcribe_gcs_with_word_time_offsets()


# %%

# TODO Next step: create a dir with gs created
