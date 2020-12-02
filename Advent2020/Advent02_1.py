def readInput(fn,makeInt=False):
    with open (fn, "r") as f:
        listInp = [x.strip () for x in f.readlines ()]
    if makeInt: listInp = [int (x) for x in listInp]
    return(listInp)

inpList = readInput("Advent02.txt")
for idx,elem in enumerate(inpList):
    inpList[idx] = elem.split(" ")

countErg = 0
for elem in inpList:
    fromCount = int(elem[0].split("-")[0])
    toCount =  int(elem[0].split("-")[1])
    countChar = 0
    for char in elem[2]:
        if char == elem[1][0]:
            countChar += 1

    if countChar >= fromCount and countChar <= toCount:
        countErg += 1
    else:
        print(elem, countChar, fromCount, toCount)
        pass
print(f"Count of matched passwords: {countErg}")
