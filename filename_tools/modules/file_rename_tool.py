# %%
import os
import pandas as pd
import asyncio

# Surpress scientific notation
# pd.reset_option('^display.', silent=True)
# pd.reset_option('display.float_format')

# def in_master_data():
#     pass


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
df_troy = df[df['']]

# %% take in directory

# read in the files of a directory

# save that list of files to a list

# parse that list and do a search on that string for the callid
# if callid is found then fileRename with the file_name value

# create a dictionary k,v
# such that the key is callID and the value is the file_name

files_list = []

for filename in os.listdir("/Users/troy/Downloads"):
    files_list.append(filename)
    pass

# print(files_list) # OK

# find .wav files
five9_calls = []

for file in files_list:
    if file.find(".wav") is not -1:
        five9_calls.append(file)

print(f"Check all wav stored...\n {five9_calls}")


# %% Dict step

# """ mvp_dict = {'key': 'value'} """

# create a new df -- contain only the values in five9_calls list

# ^^^ CURRENT PLACE / ISSUE with slicing data

# access df and get cid - not really used
callid_list = df[['callid']]

# new df of just two columns
df_CID_and_filename = df[["callid", "file_name"]]

# remove header row
df_CID_and_filename = df_CID_and_filename[1:]

# check
df_CID_and_filename  # GOOD


# turn callid into the indexing field
# df_CID_and_filename = df_CID_and_filename.set_index("callid")

# Check shape
print(df_CID_and_filename.shape)

# Check
df_CID_and_filename

# looks good

# %% Search five9_calls list for contain mvp_dict "key"
# If fiveninelist contains callid then rename to the next column filename value -- LOOP

# Find uniques

# move from df back to list
cid_master = []
filename_master = []

for index, row_data in df_CID_and_filename.iterrows():
    cid_master.append(row_data['callid'])
    filename_master.append(row_data['file_name'])
    pass

# print(cid_master)
# print(filename_master)

# Remove dupes from cid_master and then corresponding index of filename_master

# Relabel after first occurace as a dupe
for i, j in enumerate(cid_master[:-1]):
    if j == cid_master[i+1]:
        cid_master[i+1] = 'dupe'

# Check
print(f"making dupes... {cid_master}")
print(f"current length... {len(cid_master)}")

# Remove
UNIQUE_LIST = []
for i, j in enumerate(cid_master):
    # If value is not of value "dupe" then add to UNIQUE_LIST
    if j != 'dupe':
        UNIQUE_LIST.append(j)


print(f"Create unique list... {UNIQUE_LIST}")
print(f"current length... {len(UNIQUE_LIST)}")


# %%
len(cid_master)

# %%
UNIQUE_LIST = []

for i, j in enumerate(cid_master):
    if j != "dupe":
        UNIQUE_LIST.append(j)

print(UNIQUE_LIST)
# %%

DUPES_INDICIES = []

for i, j in enumerate(cid_master):
    if j == 'dupe':
        # append to indicies to delete
        DUPES_INDICIES.append(i)
print(DUPES_INDICIES)

len(DUPES_INDICIES)


# %%
del cid_master[0]
print(cid_master)
len(cid_master)

# %%
# remove list of index
for i, j in enumerate(DUPES_INDICIES):
    del cid_master[DUPES_INDICIES[i]]


print(cid_master)
# %%
print("\n")
print(cid_master)

# %%
# Example identify and remove duplicates from a list

test_list = ['a', 'a', 'b', 'c']
other_list = [1, 1, 2, 3]

for index, value in enumerate(test_list[:-1]):
    print(f"this is i.... {index}")
    print(f"this is j.... {value}")

    if value == test_list[index+1]:
        test_list[index+1] = 'dupe'

print(test_list)

# remove dupes
for i in test_list:
    if i == 'dupe':
        test_list.remove(i)

print(f"final list... {test_list}")

# %%


if i in cid_master:
    i == i+1

# %%
if __name__ == "__main__":
    in_master_data()
    pass
