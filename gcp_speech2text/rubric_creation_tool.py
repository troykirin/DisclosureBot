# Tool to create directories

# %%
import io
import os
import csv
import shutil

# %%
path_transcribe = os.getcwd()
print(path_transcribe)

# %%
# Change directory to call rubrics to save at
os.chdir("/Users/troy/APFM/ROOT_CO/Call Rubrics")

# %%
# Check
path = os.getcwd()
print(path)


# %% Open file

os.chdir(path_transcribe)
with open('./rubric_names.txt') as f:
    reader = csv.reader(f, delimiter='\n')
    for row in reader:
        print(f"Filename: {row[0]}")  # print row, access first element


# %%
