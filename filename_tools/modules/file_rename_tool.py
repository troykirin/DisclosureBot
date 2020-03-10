# %%
import os
import pandas as pd
import asyncio


def in_master_data():
    # standard header used on master reports
    standard_header = ["QA Member Name", "Report Date", "TimeOfReport", "1st_round_ref",
                       "lead_sub_stat", "callid", 'leadid', 'disclosure_date', 'calldate', 'grading_date',
                       'callType', 'timestamp', 'slaName', 'RMname', 'grade_status', 'email_sent_date',
                       'aws_link', 'file_name', 'resident_name', 'contact_name', 'property_name',
                       'property_id', 'property_email', 'sla_quote']

    df = pd.read_csv("./data/master_data.csv", names=standard_header)

    print(df)

    pass


# %% def in_master_data
standard_header = ["QA Member Name", "Report Date", "TimeOfReport", "1st_round_ref",
                   "lead_sub_stat", "callid", 'leadid', 'disclosure_date', 'calldate', 'grading_date',
                   'callType', 'timestamp', 'slaName', 'RMname', 'grade_status', 'email_sent_date',
                   'aws_link', 'file_name', 'resident_name', 'contact_name', 'property_name',
                   'property_id', 'property_email', 'sla_quote']

df = pd.read_csv(
    "/Users/troy/APFM-dev/disclosure_tools/filename_tools/data/master_data.csv", names=standard_header)


# %% # Make new dataframe just callid_slaName_lid_filename

# drop columns from dataframe and save to new one

# preserve df
orig_df = df

# list of columns to keep
keep_fields = ['callid', 'leadid', 'slaName', 'RMname', 'file_name']

# drop with list compare standard header and keep_field. else drop all else

drop_list = []

for i in standard_header:
    if i not in keep_fields:
        # .then()
        # df = df.drop([i])

        # another way possible
        drop_list.append(i)
        pass
# df.drop(drop_list)
    pass

print(drop_list)
df.drop(columns=drop_list)


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

print(cid_master)
print(filename_master)

# -- Example using enumerate
# mylist = [1, 2, 2, 4, 2, 3]
# for i, j in enumerate(mylist[:-1]):
#     if j == mylist[i+1]:
#         mylist[i] = "foo"
#         mylist[i+1] = "foo"
# print mylist
# [1, 'foo', 'foo', 4, 2, 3]


if i in cid_master:
    i == i+1

# %%
if __name__ == "__main__":
    in_master_data()
    pass
