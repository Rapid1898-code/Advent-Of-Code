import itertools

def readInput(fn,mode=0):
    """
    :param fn: input filname
    :param mode:    0 normal working => split at blank
                    1 normal int => split at blank and change to int
                    2 many lines => seperated input with empty lines,
                    3 one line / 2 values => split in char and int
    :return: list with inputs per line
    """
    with open (fn, "r") as f:
        if mode in [0,1]:
            listInp = [x.strip () for x in f.readlines ()]
        elif mode == 2:
            listInp = []
            tmpListInp = []
            for x in f.readlines():
                if x.strip() == "":
                    listInp.append(tmpListInp)
                    tmpListInp = []
                else:
                    tmpListInp.append(x.strip())
            # add last line
            listInp.append (tmpListInp)
        elif mode == 3:
            listInp = [(x.split()[0].strip(),int(x.split()[1].strip())) for x in f.readlines ()]
    if mode == 1:
        listInp = [int (x) for x in listInp]
    return(listInp)

inpList = readInput("Advent10.txt",mode=1)
inpList.sort()
print(inpList)

count1Jolt = count2Jolt = 0
count3Jolt = 1
for idxElem, contElem in enumerate(inpList):
    if idxElem == 0:
        if contElem == 3:
            count3Jolt += 1
        elif contElem == 2:
            count2Jolt += 1
        elif contElem == 1:
            count1Jolt += 1
        else:
            print (f"Wrong Difference in first Jolt: {contElem}")
    else:
        if contElem - inpList[idxElem-1] == 3:
            count3Jolt += 1
        elif contElem - inpList[idxElem-1] == 2:
            count2Jolt += 1
        elif contElem - inpList[idxElem-1] == 1:
            count1Jolt += 1
        else: print(f"Wrong Difference between Jolts from {inpList[idxElem-1]} to {contElem}")

print(f"Differences of 1 jolt: {count1Jolt}")
print(f"Differences of 2 jolt: {count2Jolt}")
print(f"Differences of 3 jolt: {count3Jolt}")
print(f"Multiplication of 1-Jolt with 3-Jolt: {count1Jolt * count3Jolt}")
print(inpList)









