# %%
# import io
import os

# Global variables
LID = '1'
CID = '2'
ResName = '3'
Date = '4'
# // these values should change value


def getInfo():
    global LID, CID, ResName, Date

    LID = input("Lead ID: ")
    CID = input("Call ID: ")
    ResName = input("Resident Name: ")
    Date = input("Date: ")
    pass


def test():
    global LID
    print(LID)
    pass


def createFileName():
    global LID, CID, ResName, Date

    # LID testing
    # -- input must be proper digits --

    # CID testing
    # --- input must be proper format

    # Date formatting
    Date = Date.replace('/', '')

    # Resident name formatting
    ResName = ResName.replace(' ', '_')  # spaces become _

    filename = print(
        "LID{}_CID{}_{}_{}".format(LID, CID, ResName, Date))


def main():
    getInfo()
    # test()
    createFileName()


# %%
if __name__ == "__main__":
    main()


# %%
