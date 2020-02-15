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
with open('./rubric_names.txt') as f:
    reader = csv.reader(f, delimiter='\n')
    count = 0
    for row in reader:
        print(f"Filename: {row[0]}")  # print row, access first element
        count += 1
        print(f"\tThis is file #{count}")

    print(f"Total file count: {count}")

# %% Duplication step
os.chdir(path_CallRubrics)


# %%
for
shutil.copy('_Template_Colorado Call Disclosure Rubric.xlsx', 'test.xls')


# %%
