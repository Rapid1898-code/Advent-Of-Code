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
    firstPos = int(elem[0].split("-")[0]) - 1
    secondPos =  int(elem[0].split("-")[1]) - 1
    countChar = 0
    if elem[1][0] == elem[2][firstPos]:
        countChar += 1
    if elem[1][0] == elem[2][secondPos]:
        countChar += 1

    if countChar == 1:
        countErg += 1
    else:
        # print(elem, countChar, firstPos, secondPos)
        pass
print(f"Count of matched passwords: {countErg}")
