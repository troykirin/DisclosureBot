# %%
import io
import pandas as pd

# %% Functions

# global vars
l1 = []
l2 = []


def readinList():
    global l1
    global l2
    df = pd.read_csv("data.csv", sep="\n", names=['A'])

    l1 = df['A'].tolist()

    df = pd.read_csv("data2.txt", sep="\n", names=['A'])
    l2 = df['A'].tolist()


def printLists():
    print(f"List 1... \n {l1}")
    print(f"List 2... \n {l2}")


def findUnique():
    global l1
    global l2

    uniqueList1 = []
    uniqueList2 = []

    for i in l1:
        if i not in uniqueList1:
            uniqueList1.append(i)

    # print("Printing uniques...\n")
    # for i in uniqueList1:
    #     print(i)

    l1 = uniqueList1

    for i in l2:
        if i not in uniqueList2:
            uniqueList2.append(i)

    l2 = uniqueList2


def findDups():
    global l1
    global l2

    dupList = []

    for i in l1:
        if i in l2:
            dupList.append(i)

    print(f"Printing dups... \n {dupList}")
    print(len(dupList))


def main():
    readinList()
    # printLists()
    findUnique()
    findDups()


# %% Main
if __name__ == "__main__":
    main()


# %%
