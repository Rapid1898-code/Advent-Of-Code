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

inpList = readInput("Advent12.txt",mode=0)
for idx, cont in enumerate(inpList):
    inpList[idx] = (inpList[idx][0],int(inpList[idx][1:]))
print(inpList)

def changeDirection (degree, direction, leftORRight):
    if degree == 90: steps = 1
    elif degree == 180: steps = 2
    elif degree == 270: steps = 3
    else: print(f"Wrong degree {degree}")

    if direction == "N": dirNr = 0
    elif direction == "E": dirNr = 1
    elif direction == "S": dirNr = 2
    elif direction == "W": dirNr = 3
    else: print(f"Wrong direction {direction}")

    if leftORRight == "L":
        for i in range(steps):
            if dirNr == 0:
                dirNr = 3
            else:
                dirNr -= 1
    if leftORRight == "R":
        for i in range(steps):
            if dirNr == 3:
                dirNr = 0
            else:
                dirNr += 1

    if dirNr == 0: return ("N")
    elif dirNr == 1: return ("E")
    elif dirNr == 2: return ("S")
    elif dirNr == 3: return ("W")
    else: print(f"Wrong dirNr {dirNr}")

direction = "E"
xSteps = 0
ySteps = 0
for inst in inpList:
    if inst[0] == "N": ySteps -= inst[1]
    if inst[0] == "S": ySteps += inst[1]
    if inst[0] == "E": xSteps += inst[1]
    if inst[0] == "W": xSteps -= inst[1]

    if inst[0] in ["L","R"]:
        direction = changeDirection(inst[1],direction,inst[0])

    if inst[0] == "F":
        if direction == "N": ySteps -= inst[1]
        if direction == "S": ySteps += inst[1]
        if direction == "E": xSteps += inst[1]
        if direction == "W": xSteps -= inst[1]

print(f"xSteps: {xSteps}")
print(f"ySteps: {ySteps}")
print(f"Manhatten Distance: {xSteps + ySteps}")


