# import itertools
#
#
# l = []
# for i in range(8):
#     l.append([0,1,2,3,4,5])
#
# print(l)
# # l = [[0,1,2,3,4,5],[0,1,2,3,4,5],[0,1,2,3,4,5],[0,1,2,3,4,5]]
# combi = list(itertools.product(*l))
#
# print(len(combi))

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

def findSides (tile):
    top = tile[0]
    bottom = tile[-1]
    left = ""
    right = ""
    for line in tile:
        left += line[0]
        right += line[-1]
    return(top, right, bottom, left)

def findMatches (key, edges, tilesDict):
    top, right, bottom, left = edges
    topLogic = False
    rightLogic = False
    bottomLogic = False
    leftLogic = False
    # print (f"\nEdges: {key, edges}")
    for keyCheck, valueCheck in tilesDict.items ():
        if keyCheck == key:
            continue
        if valueCheck[0][2] == top:
            topLogic = True
        if valueCheck[0][0] == bottom:
            bottomLogic = True
        if valueCheck[0][1] == left:
            leftLogic = True
        if valueCheck[0][3] == right:
            rightLogic = True

    # print(f"Logic: {topLogic,rightLogic,bottomLogic,leftLogic}")

    return(topLogic,rightLogic,bottomLogic,leftLogic)

def rotateTileClockwise(tile, rotate):
    rotatedTile = []
    if rotate == 90:
        tmpTileReverse = tile.copy()
        tmpTileReverse.reverse()
        for idx in range(len(tile)):
            line = ""
            for i in tmpTileReverse:
                line += i[idx]
            rotatedTile.append (line)
        return(rotatedTile)
    if rotate == 180:
        tmpTileReverse = tile.copy()
        tmpTileReverse.reverse()
        for i in tmpTileReverse:
            line = ""
            for idx in range(len(tile)-1,-1,-1):
                # print(f"IDX: {idx}")
                # print(f"Char: {i[idx]}")
                line += i[idx]
            rotatedTile.append (line)
        return(rotatedTile)
    if rotate == 270:
        tmpTileReverse = tile.copy()
        tmpTileReverse.reverse()
        for idx in range(len(tile)-1,-1,-1):
            line = ""
            for i in tmpTileReverse:
                line += i[idx]
            rotatedTile.append (line)
        return(rotatedTile)

def flippingTile(tile,direction):
    if direction == "horizontal":
        tmpTileReverse = tile.copy()
        tmpTileReverse.reverse()
        return(tmpTileReverse)
    elif direction == "vertical":
        tmpTile = tile.copy()
        for lineIDX, lineCont in enumerate(tmpTile):
            tmpTile[lineIDX] = lineCont[::-1]
        return (tmpTile)

inpTmp = readInput("Advent20.txt",mode=0)
# print(inpTmp)

tilesDict = {}
tilesDictEdge = {}
tilesEdgeLogic = {}
tileNumber = 0
tilePic = []
for elem in inpTmp:
    if "Tile" in elem:
        tileNumber = elem.split (" ")[1].replace (":", "")
    elif elem == "":
        tilesDict[tileNumber] = tilePic
        tileNumber = 0
        tilePic = []
    else:
        tilePic.append(elem)
tilesDict[tileNumber] = tilePic

for key,value in tilesDict.items():
    tmperg = list(findSides(value))
    erg = tmperg.copy()
    for i in tmperg:
        erg.append(i[::-1])
    tilesDictEdge[key] = erg

for key,val in tilesDictEdge.items():
    print(key,val)

print("\n")

workTiles = {}
matches = []
for key,val in tilesDictEdge.items():
    matches = []
    for elem in val:
        for key2,val2 in tilesDictEdge.items():
            if elem in val2 and key2 != key:
                matches.append([key2,elem])
    # print(key, matches)
    workTiles[key] = matches
smallest = 999999999
for key,val in workTiles.items():
    if len(val) < smallest:
        smallest = len(val)
    print(key,len(val),val)
print(f"Smallest: {smallest}")

multiplication = 1
for key,val in workTiles.items():
    if len(val) == smallest:
        multiplication *= int(key)
print(f"Multiplication Of Corners: {multiplication}")











