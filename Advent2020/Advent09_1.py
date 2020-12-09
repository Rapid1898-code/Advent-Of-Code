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

inpList = readInput("Advent09.txt",mode=1)
print(inpList)

preamble = 25
idx = preamble
while idx < len(inpList):
    tmpList = inpList[idx-preamble:idx]
    match = False
    for combi in itertools.combinations(tmpList, 2):
        print(combi,sum(combi))
        if sum(combi) == inpList[idx]:
            match = True
            break
    if not match:
        print(f"{inpList[idx]} has no matching pairs...")
        break
    idx += 1





