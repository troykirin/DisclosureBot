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

    LID = input()
    CID = input()
    ResName = input()
    Date = input()
    pass


def test():
    global LID
    print(LID)
    pass


def createFileName():
    global LID, CID, ResName, Date

    Date = Date.replace('/', '')
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
