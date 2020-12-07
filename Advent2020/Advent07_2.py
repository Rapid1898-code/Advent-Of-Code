def readInput(fn,mode=0):
    """
    :param fn: input filname
    :param mode: 0 normal working, 1 changed to int, 2 seperated input with empty lines
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
    if mode == 1:
        listInp = [int (x) for x in listInp]
    return(listInp)

inpList = readInput("Advent07.txt",mode=0)

bagDict = {}
for elem in inpList:
    bagKey = elem.split("contain")[0].replace("bags","").strip()
    tmpBagValues = elem.split("contain")[1].strip()
    bagValuesDict = {}
    for value in tmpBagValues.split(","):
        value = value.replace(".","").replace("bags","").replace("bag","").strip()
        bagValueName = value[1:].strip()
        bagValueAmount = value[0]
        if value[0] == "n":
            bagValuesDict["nothing"] = 0
        else:
            bagValuesDict[bagValueName] = int(bagValueAmount)
    bagDict[bagKey] = bagValuesDict

# for key, val in bagDict.items():
#     print(key, val)

# initialize ResultDict
bagsResultDict = bagDict["shiny gold"]
countBags = 0
while True:
    tmpResultDict = {}
    print(f"ResultDict Before: {bagsResultDict}")
    for Key, Val in bagsResultDict.items():
        countBags += Val
        # print (f"Key+Val: {Key, Val}")
        print(f"Content {Key, bagDict[Key]}")
        for idxTmpKey, idxTmpVal in bagDict[Key].items():
            # print(idxTmpKey,idxTmpVal, Val)
            if idxTmpVal != 0:
                if idxTmpKey in tmpResultDict:
                    tmpResultDict[idxTmpKey] += Val * idxTmpVal
                else:
                    tmpResultDict[idxTmpKey] = Val * idxTmpVal
    bagsResultDict = tmpResultDict
    print(f"ResultDictAfter: {bagsResultDict}")

    # input()

    if bagsResultDict == {}:
        break

print(bagsResultDict)
print(countBags)
