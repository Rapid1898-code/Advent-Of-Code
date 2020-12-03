def readInput(fn,makeInt=False):
    with open (fn, "r") as f:
        listInp = [x.strip () for x in f.readlines ()]
    if makeInt: listInp = [int (x) for x in listInp]
    return(listInp)

inpList = readInput("Advent03.txt")
print(inpList)

jumpList = [(1,1),(3,1),(5,1),(7,1),(1,2)]
treesMulti = 1

for combi in jumpList:
    xPos = yPos = countTrees = 0
    xJump = combi[0]
    yJump = combi[1]
    while yPos < len(inpList):
        # print(f"XPos: {xPos}, YPos: {yPos}")
        if inpList[yPos][xPos] == "#":
            countTrees += 1
        yPos += yJump
        xPos += xJump
        if xPos >= len(inpList[0]):
            xPos -= len(inpList[0])
    treesMulti *= countTrees

print(f"Multiplication of trees: {treesMulti}")



