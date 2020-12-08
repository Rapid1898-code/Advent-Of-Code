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

def runInstructions(inputList):
    idx = 0
    visited = []
    accumulator = 0
    loop = False
    while True:
        if idx in visited:
            loop = idx
            break
        if inpList[idx][0] == "nop":
            visited.append(idx)
            idx += 1
        elif inpList[idx][0] == "acc":
            accumulator += inpList[idx][1]
            visited.append (idx)
            idx += 1
        elif inpList[idx][0] == "jmp":
            visited.append (idx)
            idx += inpList[idx][1]
        else:
            print(f"Error - Wrong insturction: {inpList[idx][0]}")
    return(accumulator, loop)

inpList = readInput("Advent08.txt",mode=3)

erg = runInstructions(inpList)

print(f"Accumulated value: {erg[0]}, Loop at line: {erg[1]}")
