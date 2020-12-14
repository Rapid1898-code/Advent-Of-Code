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

inpList = readInput("Advent14.txt",mode=0)
print(inpList)
finalInpList = []
tmp = []
for i in inpList:
    if "mask" in i:
        if tmp != []:
            finalInpList.append(tmp)
        tmp = [i.split(" = ")[1]]
    else:
        tmpElem1 = int(i.split(" = ")[0][4:-1])
        tmpElem2 = int(i.split(" = ")[1])
        tmp.append((tmpElem1,tmpElem2))
finalInpList.append(tmp)
print(finalInpList)

erg = {}
for program in finalInpList:
    mask = program[0]
    for elem in program[1:]:
        valueMem = str(bin(elem[0]))[2:]
        valueMemNew = ""
        print(f"Mem Beforce Decimal: {elem[0]}")
        print(f"Mem Before: {valueMem, len(valueMem)}")
        print(f"Mask: {mask}")
        for i in range(-1,-37,-1):
            if abs (i) > len (valueMem):
                valueMemNew = mask[i] + valueMemNew
            elif mask[i] == "0":
                valueMemNew = valueMem[i] + valueMemNew
            elif mask[i] == "1":
                valueMemNew = "1" + valueMemNew
            elif mask[i] == "X":
                valueMemNew = "X" + valueMemNew
        print(f"Value After: {valueMemNew}")
        countX = valueMemNew.count("X")
        listErgMems = []
        listCombis = list(itertools.product ([0, 1], repeat=countX))
        for combi in listCombis:
            tmpvalueMemNew = valueMemNew
            for bit in combi:
                findPos = tmpvalueMemNew.find("X")
                tmpvalueMemNew = tmpvalueMemNew[:findPos] + str(bit) + tmpvalueMemNew[findPos+1:]
            listErgMems.append(tmpvalueMemNew)
        for ergMem in listErgMems:
            decMem = int(ergMem,2)
            print(f"Elem1: {elem[1]}")
            print(f"DecElem1: {decMem}")
            erg[decMem] = elem[1]

print(erg)
print(sum(erg.values()))
