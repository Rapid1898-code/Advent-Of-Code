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
        valueBinary = str(bin(elem[1]))[2:]
        valueBinaryNew = ""
        print(f"Value Beforce Decimal: {elem[1]}")
        print(f"Value Before: {valueBinary, len(valueBinary)}")
        print(f"Mask: {mask}")
        for i in range(-1,-37,-1):
            if abs(i) > len(valueBinary):
                if mask[i] == "X" or mask[i] == "0":
                    valueBinaryNew = "0" + valueBinaryNew
                elif mask[i] == "1":
                    valueBinaryNew = "1" + valueBinaryNew
            elif mask[i] == "X" or mask[i] == valueBinary[i]:
                valueBinaryNew = valueBinary[i] + valueBinaryNew
            elif mask[i] != valueBinary[i]:
                valueBinaryNew = mask[i] + valueBinaryNew
        print(f"Value After: {valueBinaryNew}")
        print(f"Value After Decimal: {int(valueBinaryNew,2)}\n")
        erg[elem[0]] = int(valueBinaryNew,2)

print(erg)
print(sum(erg.values()))
