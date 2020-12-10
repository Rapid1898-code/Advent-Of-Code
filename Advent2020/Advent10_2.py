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


listNumbersToSkip = []
idx = 0
# inpList.append(inpList[len(inpList)-1] + 3)
# inpList.insert(0,0)
print(inpList)

# inpList = [0, 3, 4, 7, 10, 11, 14, 17, 18, 19, 20, 24, 25, 28, 31, 34, 35, 38, 39, 42, 45, 46, 47, 48, 49, 52]

while True:
    if idx + 3 < len(inpList) and inpList[idx+3] == inpList[idx] + 3:
        listNumbersToSkip.append(inpList[idx+1])
        listNumbersToSkip.append(inpList[idx+2])
        idx += 3
    elif idx + 2 < len(inpList) and inpList[idx+2] == inpList[idx] + 2:
        listNumbersToSkip.append(inpList[idx+1])
        idx += 2
    else: idx += 1
    if idx == len(inpList):
        break

print(listNumbersToSkip)
erg = 1
for i in range(1,len(listNumbersToSkip)+1):
    erg *= i
print(erg + 2)


