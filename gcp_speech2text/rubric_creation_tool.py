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
path_CallRubrics = "/Users/troy/APFM/ROOT_CO/Call Rubrics"

os.chdir(path_CallRubrics)

# %%
# Check
path = os.getcwd()
print(path)


# %% Open file
os.chdir(path_transcribe)

# get number of files to create
numOfFiles = 0
fileList = []

with open('./rubric_names.txt') as f:
    reader = csv.reader(f, delimiter='\n')
    count = 0
    for row in reader:
        print(f"Filename: {row[0]}")  # print row, access first element
        fileList.append(row[0])
        count += 1
        print(f"\tThis is file #{count}")

    print(f"Total file count: {count}")
    numOfFiles = count


# %%
print(fileList[0])

# %%
os.chdir(path_CallRubrics)

for element in fileList:
    # get filename
    filename = element + ".xlsx"
    # creation
    shutil.copy('_Template_Colorado Call Disclosure Rubric.xlsx', filename)

    # %%
