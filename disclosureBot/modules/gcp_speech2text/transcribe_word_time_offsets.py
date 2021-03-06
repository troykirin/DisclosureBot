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

# --- Imports ---
# import argparse
# import io
import csv
import os
# import errno

from google.oauth2 import service_account


# Class variable
URI_LIST = ['yee']

# Credentials for google cloud account
credentials = service_account.Credentials.from_service_account_file(
    '/Users/troy/APFM-dev/gcp-transcribe-api-key.json')


def get_cloud_files():

    global URI_LIST

    # Read in csv list
    with open('/Users/troy/APFM-dev/disclosure_tools/gcp_speech2text/gcp_transcribe_list.csv', 'r') as infile:
        reader = csv.reader(infile)
        URI_LIST = list(reader)

    # Flatten list
    flat_list = [
        item for sublist in URI_LIST for item in sublist]

    pass


def run_the_cloud():
    # take uri list - chk

    global URI_LIST

    print("starting to run the cloud.... \n")

    # pass into transcription function
    for item in URI_LIST:
        transcribe_gcs_with_word_time_offsets(gcs_uri=item, language='en-US')
        print(f"Just ran {item}")

    # itereate until consume entire uri list
    pass


def transcribe_gcs_with_word_time_offsets(gcs_uri, language):
    """Transcribe the given audio file asynchronously and output the word time offsets."""

    # - STABLE BUILD -

    # from google.cloud import speech
    # from google.cloud.speech import enums
    # from google.cloud.speech import types

    # - BETA BUILD -
    from google.cloud import speech_v1p1beta1
    from google.cloud.speech_v1p1beta1 import enums
    from google.cloud.speech_v1p1beta1 import types

    # -- MAY NEED TO REMOVE ---
    # # Default language to use
    # language = 'en-US'

    # # Ask user for gcs_uri
    # gcs_uri = input("Please enter gcs_uri: ")

    # # Print to confirm
    # print("You just entered: ", gcs_uri)

    # ___ END ___ OF MAY ^^^^

    # client = speech.SpeechClient()  # STABLE
    client = speech_v1p1beta1.SpeechClient(credentials=credentials)  # BETA

    # list of phrases to use in boost
    phrases = []

    with open('/Users/troy/APFM-dev/disclosure_tools/gcp_speech2text/disclosure_phrases.csv', 'r') as f:
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

    # --- MY Unique Solution to Improve Accuracy of Transcriptions ---
    # create a dataframe
    # have a matrix of SLA to their corresponding phrases (essentially a dictionary of k,v pairs)
    # maybe a scenario of frequent itemset mining where if A shows up then what's the probability of B showing up
    # the A being "great, thank you" could boost probability of that being the start of next phrases too

    # The dataframe would also have a very high boost for the name of lead from database
    # read in the csv of lead helping, there is a very high probability name will show up in first sentance, essentially first 5-6 seconds.

    # dataframe should also have feature to have stopword list. -- words that should be ignored in this scenario.
    # something like "bye" kept showing up which is supposed to obviously be "by" in the conext we are using this solution for

    # the chatbot thought
    # if we think about it, essentially the conversation is a simple decison tree.
    # if this then this.
    # when first phrase matches expected output then end / catagorize as speaker 1.
    # then start speaker 2, listen for affirmative yes.
    # we can define a list of phrases that correspond to an affirmative yes.
    # ex. yes,sure,mhmm,okay,that's fine. --- there already exists corpus of this nature.
    # the vision
    # if we use a bot to listen to the disclosure call when the SLA click a button. It will initiate a streaming transcription. When this happens there will need to be a live confirmation that happens DURING the call and not POST.
    # this is a solution that provides the following
    # 1. real-time conversation intelligence
    # 2. reduce overhead of communication of QA disclosure grading, sending email to RM, RM reaching out to SLA, SLA needing to work on getting a hold of lead.
    # 3. Reduce the lead lost rate, if they are not willing to continue working with APFM after first attempt.
    # Question: What is the cost of having to fail a disclosure and getting 2nd disclosure?
    # Where can you find data to support this hypothesis
    # What kind of effective presentation would prove this solution as something to provide value to both the company and clients?

    # --- END ---

    # Form 1
    config = {
        # "encoding": enums.RecognitionConfig.AudioEncoding.LINEAR16,
        "encoding": "MP3",
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

    pathDir = "/Users/troy/APFM-dev/disclosure_tools/gcp_speech2text/transcriptions/03-09/"

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
    # transcript_file.write("Below is transcript: for {}\n".format(gcs_uri))

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
            f"{alternative.transcript} \n")

        print('Confidence: {} \n'.format(alternative.confidence))
        # transcript_file.write(
        # 'Confidence Score: {} \n'.format(alternative.confidence))

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

    get_cloud_files()
    run_the_cloud()

    # transcribe_gcs_with_word_time_offsets()


# %%

# TODO Next step: create a dir with gs created


# %%


# %%
