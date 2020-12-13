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

inpList = readInput("Advent12.txt",mode=0)
for idx, cont in enumerate(inpList):
    inpList[idx] = (inpList[idx][0],int(inpList[idx][1:]))
print(inpList)

waypoint = [["E",10],["N",1]]
shipPoint = [["E",0],["N",0]]
for inst in inpList:
    if waypoint[0][0] in ["E", "W"]:
        if inst[0] == "N":
            if waypoint[1][0] == "N":
                waypoint[1][1] += inst[1]
            elif waypoint[1][0] == "S":
                if inst[1] > waypoint[1][1]:
                    waypoint[1][0] = "N"
                    waypoint[1][1] = inst[1] - waypoint[1][1]
                else:
                    waypoint[1][1] -= inst[1]
        if inst[0] == "S":
            if waypoint[1][0] == "S":
                waypoint[1][1] += inst[1]
            elif waypoint[1][0] == "N":
                if inst[1] > waypoint[1][1]:
                    waypoint[1][0] = "S"
                    waypoint[1][1] = inst[1] - waypoint[1][1]
                else:
                    waypoint[1][1] -= inst[1]
        if inst[0] == "E":
            if waypoint[0][0] == "E":
                waypoint[0][1] += inst[1]
            elif waypoint[0][0] == "W":
                if inst[1] > waypoint[0][1]:
                    waypoint[0][0] = "E"
                    waypoint[0][1] = inst[1] - waypoint[0][1]
                else:
                    waypoint[0][1] -= inst[1]
        if inst[0] == "W":
            if waypoint[0][0] == "W":
                waypoint[0][1] += inst[1]
            elif waypoint[0][0] == "E":
                if inst[1] > waypoint[0][1]:
                    waypoint[0][0] = "W"
                    waypoint[0][1] = inst[1] - waypoint[0][1]
                else:
                    waypoint[0][1] -= inst[1]
    elif waypoint[0][0] in ["N", "S"]:
        if inst[0] == "N":
            if waypoint[0][0] == "N":
                waypoint[0][1] += inst[1]
            elif waypoint[0][0] == "S":
                if inst[1] > waypoint[0][1]:
                    waypoint[0][0] = "N"
                    waypoint[0][1] = inst[1] - waypoint[0][1]
                else:
                    waypoint[0][1] -= inst[1]
        if inst[0] == "S":
            if waypoint[0][0] == "S":
                waypoint[0][1] += inst[1]
            elif waypoint[0][0] == "N":
                if inst[1] > waypoint[0][1]:
                    waypoint[0][0] = "S"
                    waypoint[0][1] = inst[1] - waypoint[0][1]
                else:
                    waypoint[0][1] -= inst[1]
        if inst[0] == "E":
            if waypoint[1][0] == "E":
                waypoint[1][1] += inst[1]
            elif waypoint[1][0] == "W":
                if inst[1] > waypoint[1][1]:
                    waypoint[1][0] = "E"
                    waypoint[1][1] = inst[1] - waypoint[1][1]
                else:
                    waypoint[1][1] -= inst[1]
        if inst[0] == "W":
            if waypoint[1][0] == "W":
                waypoint[1][1] += inst[1]
            elif waypoint[1][0] == "E":
                if inst[1] > waypoint[1][1]:
                    waypoint[1][0] = "W"
                    waypoint[1][1] = inst[1] - waypoint[1][1]
                else:
                    waypoint[1][1] -= inst[1]
    else: print(f"Wrong direction waypoint {waypoint[0][0]}")

    if inst[0] in ["L","R"]:
        waypoint[0][0] = changeDirection (inst[1], waypoint[0][0], inst[0])
        waypoint[1][0] = changeDirection (inst[1], waypoint[1][0], inst[0])

    if inst[0] == "F":
        for wp in waypoint:
            diff = wp[1] * inst[1]
            if wp[0] == "N":
                if shipPoint[1][0] == "N":
                    shipPoint [1][1] += diff
                elif shipPoint[1][0] == "S":
                    if diff > shipPoint [1][1]:
                        shipPoint[1][0] = "N"
                        shipPoint[1][1] = diff - shipPoint[1][1]
                    else:
                        shipPoint[1][1] -= diff
            if wp[0] == "S":
                if shipPoint[1][0] == "S":
                    shipPoint [1][1] += diff
                elif shipPoint[1][0] == "N":
                    if diff > shipPoint [1][1]:
                        shipPoint[1][0] = "S"
                        shipPoint[1][1] = diff - shipPoint[1][1]
                    else:
                        shipPoint[1][1] -= diff
            if wp[0] == "E":
                if shipPoint[0][0] == "E":
                    shipPoint [0][1] += diff
                elif shipPoint[0][0] == "W":
                    if diff > shipPoint [0][1]:
                        shipPoint[0][0] = "E"
                        shipPoint[0][1] = diff - shipPoint[0][1]
                    else:
                        shipPoint[0][1] -= diff
            if wp[0] == "W":
                if shipPoint[0][0] == "W":
                    shipPoint [0][1] += diff
                elif shipPoint[0][0] == "E":
                    if diff > shipPoint [0][1]:
                        shipPoint[0][0] = "W"
                        shipPoint[0][1] = diff - shipPoint[0][1]
                    else:
                        shipPoint[0][1] -= diff

    print(f"Instruction: {inst}")
    print(f"Waypoint: {waypoint}")
    print (f"ShipPoint: {shipPoint}\n")

print (f"ShipPoint: {shipPoint}")
print(f"Manhatten Distance: {shipPoint[0][1] + shipPoint[1][1]}")
