# %%
import os
from os import path
import pandas as pd
import numpy as np
import asyncio

# Surpress scientific notation
# pd.reset_option('^display.', silent=True)
# pd.reset_option('display.float_format')

# def in_master_data():
#     pass

# Set path
if path.exists("/Users/troy/Downloads/"):
    DOWNLOADS_PATH = "/Users/troy/Downloads/"

# Change Path / Working Directory
os.chdir(DOWNLOADS_PATH)

# %% test OS RENAME
# os.rename(DOWNLOADS_PATH+"pathfinder.wav",DOWNLOADS_PATH+"test.wav")
os.rename("test.wav", "devPath_BotDev.wav")

# %% Read in data

# -- CURRENTLY Requires manually delete first two header rows,
# from csv export from master sheet

df = pd.read_csv(
    "/Users/troy/APFM-dev/disclosure_tools/filename_tools/data/master_data2.csv")
df

# %% Get Names
df.columns

# %% Drop Non Primary Columns

# preserve df
ORIG_DF = df

# list of columns to keep
KEEP_FIELDS = ['QA Team Member Name', 'Report Date',
               'Call ID #', 'SLA Name', 'RM Name', 'File Name']

# drop with list compare standard header and keep_field. else drop all else
DROP_LIST = []

for i in df.columns:
    if i not in KEEP_FIELDS:
        # .then()
        # df = df.drop([i])

        # another way possible
        DROP_LIST.append(i)
        pass
# df.drop(drop_list)
    pass

print(DROP_LIST)
df.drop(columns=DROP_LIST)


# %% Get only Troy Kirin's Records

# Get indicies
incidies_df = df[df['QA Team Member Name'] != 'Troy Kirinhakone'].index

# Delete else
df.drop(incidies_df, inplace=True)

df

# %% Gather info from local

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

# Validation
print(f"Check all wav stored...\n {FIVE9_CALLS}")


# %% Slice Dataframe to CID + Filename

# create df_rename contain 'Call ID #' and 'File Name'
df_rename = df[["Call ID #", "File Name"]]

# Validation
print(df_rename)
print(df_rename.shape)

# %% Prepare lists for rename

# Drop any records of duplicate File Names
df_rename.drop_duplicates(subset='File Name', inplace=True)
df_rename

# Drop Nan CID - Missing CID Case
# Drop Nan FileName & Please find call id
df_rename = df_rename.dropna(axis=0)

# %% Rename file step

# Convert dataframe into a list of lists
RENAME_REF_LIST = df_rename.values.tolist()

# # Test
# # Get first CID from RENAME_REF_LIST
# print(RENAME_REF_LIST[0][0])
# # Get frist File Name from RENAME_REF_LIST
# print(RENAME_REF_LIST[0][1])

# If five9 list contains cid from rename rereferralist
# then rename with filename in col 2

# %% test
for file in FIVE9_CALLS:
    for record in RENAME_REF_LIST:
        if file.find(record[0]) is not -1:
            os.rename()
    pass
pass

# %%
if __name__ == "__main__":
    # master_switch()
    pass
