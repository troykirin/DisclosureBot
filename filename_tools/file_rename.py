# file rename in directory given a list

# ------ PSEUDOCODE -----

# csv in directory contains list of call ids
# csv in dir contains filenames

# string manipulate file_id to grab only cid

# walk file_name string until cid is found.
# save the next 8 digits int format

# do a comparisson between list1_CIDS && list2_fileNames

# saves those two into a dataframe

# do a grab files in directory and list them
# save that intoa list
# -- this will be the downloaded files from five9

# display / print all these in a dataframe.
# this will be an 8 by 3 matrix at this point.

# the dataframe needs to be sorted so that a series of "files downloaded from five9" aligns with the cid
# --- CID should already match the filename at this point

# loop and do a rename "bash mv command"
# of the files downloaded to the filename


# ^^^ that is the mvp


# once that is done, iteration 2 of the script

# --- be able to pull activesheet for the day from google sheets.

# do a pull of all the entries containing input name
# "Troy" in column A

# this will generate the script to seek filenames in download directory from five9
# then do the rename based on master sheet.

# --- DONE ---
