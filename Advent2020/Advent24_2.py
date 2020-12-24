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

inpErg = []
inpTmp = readInput("Advent24.txt",mode=0)
for elem in inpTmp:
    idx=0
    elemList = []
    while idx < len(elem):
        if elem[idx] in ["e","w"]:
            elemList.append(elem[idx])
            idx += 1
        else:
            elemList.append(elem[idx:idx+2])
            idx += 2
    inpErg.append(elemList)
# for i in inpErg:
#     print(i)

ergList = []
for elem in inpErg:
    xIDX = 0
    yIDX = 0
    rowIDX = 0
    for direction in elem:
        if direction == "e":
            xIDX += 1
        elif direction == "w":
            xIDX -= 1
        elif direction == "sw":
            yIDX += 1
            rowIDX += 1
            if rowIDX % 2 == 0:
                xIDX -= 1
        elif direction == "nw":
            yIDX -= 1
            rowIDX -= 1
            if rowIDX % 2 == 0:
                xIDX -= 1
        elif direction == "se":
            yIDX += 1
            rowIDX += 1
            if rowIDX % 2 == 1:
                xIDX += 1
        elif direction == "ne":
            yIDX -= 1
            rowIDX -= 1
            if rowIDX % 2 == 1:
                xIDX += 1
        else:
            print(f"Wrong direction: {direction}")

    if (xIDX,yIDX) in ergList:
        ergList.remove((xIDX,yIDX))
    else:
        ergList.append((xIDX,yIDX))
    print(f"Actual Black Hexagons: {ergList}")
    # input()
print(f"Count of black Hexagons: {len(ergList)}")
print(f"Max: {max(ergList)}")
print(f"Min: {min(ergList)}")
