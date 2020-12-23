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

def rotate(l, n):
    return l[-n:] + l[:-n]

inpTmp = readInput("Advent23.txt",mode=0)
cupListTemp = list(map(int, list(inpTmp[0])))
round = 1
maxRound = 10000000
currentCupIDX = -1
tmpList = [i for i in range(1000001)]
cupList = cupListTemp + tmpList
del cupList[9:19]
lowestCup = min(cupList)
highestCup = max(cupList)

while round <= maxRound:
    print(f"\nRound: {round+1}")
    # print(f"Actual Cups {cupList}")
    tmpCupList = cupList.copy()
    currentCupIDX += 1
    if currentCupIDX >= len(cupList):
        currentCupIDX = 0
    currentCup = cupList[currentCupIDX]

    list3Cups = []
    if currentCupIDX + 1 >= len(cupList):
        first3CupIDX = currentCupIDX + 1 - len(cupList)
    else:
        first3CupIDX = currentCupIDX + 1
    if currentCupIDX + 2 >= len(cupList):
        second3CupIDX = currentCupIDX + 2 - len(cupList)
    else:
        second3CupIDX = currentCupIDX + 2
    if currentCupIDX + 3 >= len(cupList):
        third3CupIDX = currentCupIDX + 3 - len(cupList)
    else:
        third3CupIDX = currentCupIDX + 3
    first3Cup = cupList[first3CupIDX]
    second3Cup = cupList[second3CupIDX]
    third3Cup = cupList[third3CupIDX]
    list3Cups.extend([first3Cup,second3Cup,third3Cup])
    tmpCupList.remove(first3Cup)
    tmpCupList.remove(second3Cup)
    tmpCupList.remove(third3Cup)

    # print(f"CurrentCup, Cup 1-2-3: {currentCup,first3Cup,second3Cup,third3Cup}")
    # print(f"CurrentCupIDX, CupIDX 1-2-3: {currentCup,first3CupIDX,second3CupIDX,third3CupIDX}")
    # print(f"Current Cup: {currentCup}")
    # print(f"List3Cups Pickup: {list3Cups}")

    # find destination cup
    if currentCup - 1 < lowestCup:
        destinationCup = highestCup
    else:
        destinationCup = currentCup - 1
    while True:
        if destinationCup not in list3Cups:
            break
        if destinationCup - 1 < lowestCup:
            destinationCup = highestCup
        else:
            destinationCup -= 1

    destinationCupIDX = tmpCupList.index(destinationCup)
    if destinationCupIDX + 1 >= len(cupList):
        tmpCupList.insert (destinationCupIDX + 1 - len(cupList), first3Cup)
    else:
        tmpCupList.insert(destinationCupIDX + 1, first3Cup)
    if destinationCupIDX + 2 >= len(cupList):
        tmpCupList.insert (destinationCupIDX + 2 - len(cupList), second3Cup)
    else:
        tmpCupList.insert(destinationCupIDX + 2, second3Cup)
    if destinationCupIDX + 3 >= len(cupList):
        tmpCupList.insert (destinationCupIDX + 3 - len(cupList), third3Cup)
    else:
        tmpCupList.insert(destinationCupIDX + 3, third3Cup)
    # print(f"Destination Cup: {destinationCup}")
    # input()

    round += 1
    while tmpCupList[currentCupIDX] != currentCup:
        # print(f"WorkingList: {tmpCupList}")
        # print(f"tmpCupList[currentCupIDX]: {tmpCupList[currentCupIDX]}")
        # print(f"Currentcup: {currentCup}")
        # input()
        tmpCupList = rotate(tmpCupList,1)

    cupList = tmpCupList.copy()

# print(f"CupList Before: {cupList}")
while cupList[0] != 1:
    print(cupList)
    cupList = rotate(cupList,1)
cupList.pop(0)
# print(cupList)
cupList = list(map(str,cupList))
erg = ''.join(cupList)
print(f"ResultString: {erg}")
