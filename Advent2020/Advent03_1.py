def readInput(fn,makeInt=False):
    with open (fn, "r") as f:
        listInp = [x.strip () for x in f.readlines ()]
    if makeInt: listInp = [int (x) for x in listInp]
    return(listInp)

inpList = readInput("Advent03.txt")
print(inpList)

xPos = yPos = countTrees = 0
while yPos < len(inpList):

    # print(f"XPos: {xPos}, YPos: {yPos}")

    if inpList[yPos][xPos] == "#":
        countTrees += 1
    yPos += 1
    xPos += 3
    if xPos >= len(inpList[0]):
        xPos -= len(inpList[0])
print(f"Count of trees: {countTrees}")



