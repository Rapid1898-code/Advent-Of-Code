
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

inpTmp = readInput("Advent15.txt",mode=0)
inpList = []
for i in inpTmp[0].split(","):
    inpList.append(int(i))
print(inpList)

erg = ["start"]
ergDict = {}
duration = 30000000

for idx, elem in enumerate(inpList):
    erg.append(elem)
    if idx < len(inpList)-1:
        ergDict[elem] = [idx+1,-1]
# print(erg)
# print(ergDict)

for i in range(len(inpList)+1, duration+1, 1):
    # Aktualisierung Dict
    if erg[-1] not in ergDict:
        ergDict[erg[-1]] = [i-1,-1]
        erg.append(0)
    elif ergDict[erg[-1]][1] == -1:
        ergDict[erg[-1]][1] = i - 1
        erg.append(ergDict[erg[-1]][1] - ergDict[erg[-1]][0])
    elif ergDict[erg[-1]][1] != -1:
        ergDict[erg[-1]][0] = ergDict[erg[-1]][1]
        ergDict[erg[-1]][1] = i - 1
        erg.append (ergDict[erg[-1]][1] - ergDict[erg[-1]][0])
    print(f"Round: {i}")
print(f"Erg: {erg[-1]}")
# print(f"ErgDict: {ergDict}")


