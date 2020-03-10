import os
from os import path
import pandas as pd
import numpy as np
import asyncio


def master_switch():

    # Set path
    if path.exists("/Users/troy/Downloads/"):
        DOWNLOADS_PATH = "/Users/troy/Downloads/"

    # Change Path / Working Directory
    os.chdir(DOWNLOADS_PATH)

    # ___ Read in data ___

    # --- NOTE!! ---
    # CURRENTLY Requires manually delete first two header rows,
    # from csv export from master sheet

    df = pd.read_csv(
        "/Users/troy/APFM-dev/disclosure_bot/data/master_data.csv")

    # __Drop Non Primary Columns__

    # list of columns to keep
    KEEP_FIELDS = ['QA Team Member Name', 'Report Date',
                   'Call ID #', 'SLA Name', 'RM Name', 'File Name']

    # drop with list compare standard header and keep_field. else drop all else
    DROP_LIST = []

    for i in df.columns:
        if i not in KEEP_FIELDS:
            DROP_LIST.append(i)

    df.drop(columns=DROP_LIST)

    # __Get only Troy Kirin's Records__

    # Get indicies
    incidies_df = df[df['QA Team Member Name'] != 'Troy Kirinhakone'].index

    # Delete else
    df.drop(incidies_df, inplace=True)

    # __Gather info from local__

    # Files list
    files_list = []

    # Get all files in Downloads Dir
    for filename in os.listdir("/Users/troy/Downloads"):
        files_list.append(filename)
        pass

    # Apend filename of five9 calls
    FIVE9_CALLS = []

    # If file is .wav type then append filename onto list
    for file in files_list:
        if file.find(".wav") is not -1:
            FIVE9_CALLS.append(file)

    # __Slice Dataframe to CID + Filename__

    # create df_rename contain 'Call ID #' and 'File Name'
    df_rename = df[["Call ID #", "File Name"]]

    # __Prepare lists for rename__

    # Drop any records of duplicate File Names
    df_rename = df_rename.drop_duplicates(subset='File Name')

    # Drop Nan CID - Missing CID Case
    # Drop Nan FileName & Please find call id
    df_rename = df_rename.dropna(axis=0)

    # %% Rename file step

    # Convert dataframe into a list of lists
    RENAME_REF_LIST = df_rename.values.tolist()

    # Rename Loop
    for file in FIVE9_CALLS:
        for record in RENAME_REF_LIST:
            if file.find(record[0]) is not -1:
                os.rename(file, record[1] + ".wav")


if __name__ == "__main__":
    master_switch()
