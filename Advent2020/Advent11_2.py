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

inpList = readInput("Advent11.txt",mode=0)
for i in inpList: print(i)
print("\n")

def checkOccupiedSeats (listPlan, xPos, yPos):
    occupied = 0
    noUp = noDown = noLeft = noRight = False    
    if yPos == 0: 
        noUp = True
    if xPos == 0:
        noLeft = True
    if yPos == len(listPlan)-1:
        noDown = True
    if xPos == len(listPlan[0])-1:
        noRight = True

    if not noUp:
        tmpOccupied = False
        tmpYPos = yPos-1
        while tmpYPos >= 0:
            if listPlan[tmpYPos][xPos] == "L":
                break
            elif listPlan[tmpYPos][xPos] == "#":
                tmpOccupied = True
                break
            tmpYPos -= 1
        if tmpOccupied: occupied +=1

    if not noUp and not noRight:
        tmpOccupied = False
        tmpYPos = yPos-1
        tmpXPos = xPos+1
        while tmpYPos >= 0 and tmpXPos < len(listPlan[0]):
            if listPlan[tmpYPos][tmpXPos] == "L":
                break
            elif listPlan[tmpYPos][tmpXPos] == "#":
                tmpOccupied = True
                break
            tmpYPos -= 1
            tmpXPos += 1
        if tmpOccupied: occupied += 1

    if not noRight:
        tmpOccupied = False
        tmpXPos = xPos+1
        while tmpXPos < len(listPlan[0]):
            if listPlan[yPos][tmpXPos] == "L":
                break
            elif listPlan[yPos][tmpXPos] == "#":
                tmpOccupied = True
                break
            tmpXPos += 1
        if tmpOccupied: occupied +=1

    if not noDown and not noRight:
        tmpOccupied = False
        tmpYPos = yPos+1
        tmpXPos = xPos+1
        while tmpXPos < len(listPlan[0]) and tmpYPos < len(listPlan):
            if listPlan[tmpYPos][tmpXPos] == "L":
                break
            elif listPlan[tmpYPos][tmpXPos] == "#":
                tmpOccupied = True
                break
            tmpYPos += 1
            tmpXPos += 1
        if tmpOccupied: occupied += 1

    if not noDown:
        tmpOccupied = False
        tmpYPos = yPos+1
        while tmpYPos < len(listPlan):
            if listPlan[tmpYPos][xPos] == "L":
                break
            elif listPlan[tmpYPos][xPos] == "#":
                tmpOccupied = True
                break
            tmpYPos += 1
        if tmpOccupied: occupied +=1

    if not noDown and not noLeft:
        tmpOccupied = False
        tmpYPos = yPos+1
        tmpXPos = xPos-1
        while tmpXPos >= 0 and tmpYPos < len(inpList):
            if listPlan[tmpYPos][tmpXPos] == "L":
                break
            elif listPlan[tmpYPos][tmpXPos] == "#":
                tmpOccupied = True
                break
            tmpYPos += 1
            tmpXPos -= 1
        if tmpOccupied: occupied += 1

    if not noLeft:
        tmpOccupied = False
        tmpXPos = xPos-1
        while tmpXPos >= 0:
            if listPlan[yPos][tmpXPos] == "L":
                break
            elif listPlan[yPos][tmpXPos] == "#":
                tmpOccupied = True
                break
            tmpXPos -= 1
        if tmpOccupied: occupied +=1

    if not noLeft and not noUp:
        tmpOccupied = False
        tmpYPos = yPos-1
        tmpXPos = xPos-1
        while tmpXPos >= 0 and tmpYPos >= 0:
            if listPlan[tmpYPos][tmpXPos] == "L":
                break
            elif listPlan[tmpYPos][tmpXPos] == "#":
                tmpOccupied = True
                break
            tmpYPos -= 1
            tmpXPos -= 1
        if tmpOccupied: occupied += 1
    return(occupied)

idxRound = 1
while True:
    tmpPlan = inpList.copy()
    for xPos in range(len(inpList[0])):
        for yPos in range(len(inpList)):
            if inpList[yPos][xPos] == ".":
                continue
            elif inpList[yPos][xPos] == "L":
                # print(f"Drinnen - Check {xPos, yPos}")
                countOccupied = checkOccupiedSeats(inpList, xPos, yPos)
                if countOccupied == 0:
                    tmpPlan[yPos] = tmpPlan[yPos][:xPos] + "#" + tmpPlan[yPos][xPos+1:]
            elif inpList[yPos][xPos] == "#":
                countOccupied = checkOccupiedSeats(inpList, xPos, yPos)
                if countOccupied >= 5:
                    tmpPlan[yPos] = tmpPlan[yPos][:xPos] + "L" + tmpPlan[yPos][xPos+1:]
            else: print(f"Wrong Character at Position X:{xPos} and Y:{yPos} with Char:{inpList[yPos][xPos]}")
    print(f"\nRound {idxRound}")
    idxRound += 1
    for i in tmpPlan: print (i)
    if inpList == tmpPlan:
        break
    inpList = tmpPlan.copy()

countSeatedPlaces = 0
for row in tmpPlan:
    for cell in row:
        if cell == "#":
            countSeatedPlaces += 1
print(f"\nFinal Seating Place:")
for i in tmpPlan: print(i)
print(f"Seated Places: {countSeatedPlaces}")

