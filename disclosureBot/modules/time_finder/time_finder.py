# time_finder

# %%
import os
from os import path
import pandas as pd

test_data_path = "/Users/troy/APFM-dev/disclosure_bot/disclosureBot/modules/time_finder"

if path.exists(test_data_path):
    data = test_data_path
    print("Path is good!")
else:
    raise Exception("The path does not exist!")

# %%
print(os.getcwd())


# %%
df = pd.read_csv("./test_data/test_five9_call_data.csv")

# %%
df

# %%
