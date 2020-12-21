import math

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

def arrangeTile(tile1, tile2, tileEdge1, tileEdge2, matchSide, tile3=0, tileEdge3=0):
    match = list (set (tileEdge1) & set (tileEdge2))
    if matchSide == "LeftCorner":
        match2 = list (set (tileEdge1) & set (tileEdge3))
        while findSides(tile1)[1] not in match or findSides(tile1)[2] not in match2:
            tile1 = rotateTileClockwise (tile1, 90)
            print (f"Tile1: Found Right Side: {findSides (tile1)[1]}")
            print (f"Tile1: Found: {tile1}")
            print (f"Tile1: Found Bottom Side: {findSides (tile1)[2]}")
            print (f"Tile1: Found: {tile2}")
    if matchSide == "R":
        while findSides (tile1)[1] not in match:
            # print(f"Right Side: {findSides(tile1)[1]}")
            tile1 = rotateTileClockwise (tile1, 90)
        print (f"Tile1: Found Right Side: {findSides (tile1)[1]}")
        print (f"Tile1: Found: {tile1}")

        while findSides (tile2)[3] not in match:
            # print(f"Right Side: {findSides(tile1)[3]}")
            tile2 = rotateTileClockwise (tile2, 90)
        print (f"Tile1: Found Right Side: {findSides (tile2)[3]}")
        print (f"Tile1: Found: {tile2}")


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

tilesCorners = []
tilesEdges = []
tilesInner = []
workTiles = {}
matches = []
tilesMatches = {}
for key,val in tilesDictEdge.items():
    matches = []
    tmpMatchesTiles = []
    for elem in val:
        for key2,val2 in tilesDictEdge.items():
            if elem in val2 and key2 != key:
                matches.append([key2,elem])
                tmpMatchesTiles.append(key2)
    # print(key, matches)
    workTiles[key] = matches
    tilesMatches[key] = tmpMatchesTiles

for key,val in workTiles.items():
    if len(val) == 4 and key not in tilesCorners:
        tilesCorners.append(key)
    elif len(val) == 6 and key not in tilesEdges:
        tilesEdges.append(key)
    elif len (val) == 8 and key not in tilesInner:
        tilesInner.append (key)
    else:
        print(f"Wrong Length of Tiles with value {len(val)}")

# for key,val in tilesDictEdge.items():
#     print(key,val)
# for key,val in tilesMatches.items():
#     print(key,val)
print(f"Corner Tiles: {len(tilesCorners), tilesCorners}")
print(f"Edge Tiles: {len(tilesEdges), tilesEdges}")
print(f"Inner Tiles: {len(tilesInner), tilesInner}")
widthOfPic = int(math.sqrt(len(tilesCorners) + len(tilesEdges) + len(tilesInner)))
print(f"Width of Pic: {widthOfPic}")

ergPic = {}
#make frame for pic
xIDX = 0
yIDX = 0
# start with first corner element
ergPic[xIDX,yIDX] = tilesCorners[0]
tilesCorners.pop(0)
# # start with last corner element
# ergPic[xIDX,yIDX] = tilesCorners[-1]
# tilesCorners.pop()

# build top line of edge
while xIDX < widthOfPic:
    xIDX += 1
    found = False
    for i in tilesEdges:
        if ergPic[xIDX-1,yIDX] in tilesMatches[i]:
            ergPic[xIDX,yIDX] = i
            found = True
            break
    if found:
        tilesEdges.remove (i)
    else:
        for i in tilesCorners:
            if ergPic[xIDX - 1, yIDX] in tilesMatches[i]:
                ergPic[xIDX, yIDX] = i
                xIDX += 1
                tilesCorners.remove (i)
                break

# build left line of edge
xIDX = 0
while yIDX < widthOfPic:
    yIDX +=1
    found = False
    for i in tilesEdges:
        if ergPic[xIDX,yIDX-1] in tilesMatches[i]:
            ergPic[xIDX,yIDX] = i
            found = True
            break
    if found:
        tilesEdges.remove (i)
    else:
        for i in tilesCorners:
            if ergPic[xIDX, yIDX-1] in tilesMatches[i]:
                ergPic[xIDX, yIDX] = i
                yIDX += 1
                tilesCorners.remove (i)
                break

# build right line of edge
xIDX = widthOfPic-1
yIDX = 0
while yIDX < widthOfPic:
    yIDX +=1
    found = False
    for i in tilesEdges:
        if ergPic[xIDX,yIDX-1] in tilesMatches[i]:
            ergPic[xIDX,yIDX] = i
            found = True
            break
    if found:
        tilesEdges.remove (i)
    else:
        for i in tilesCorners:
            if ergPic[xIDX, yIDX-1] in tilesMatches[i]:
                ergPic[xIDX, yIDX] = i
                yIDX += 1
                tilesCorners.remove (i)
                break

# build bottom line of edge
xIDX = 0
yIDX = widthOfPic-1
while tilesEdges != []:
    xIDX +=1
    found = False
    for i in tilesEdges:
        if ergPic[xIDX-1,yIDX] in tilesMatches[i]:
            ergPic[xIDX,yIDX] = i
            found = True
            break
    if found:
        tilesEdges.remove (i)

# build inner pic
widthInner = int(math.sqrt(len(tilesInner)))
for xIDX in range(1,widthInner + 1, 1):
    for yIDX in range (1, widthInner + 1, 1):
        found = False
        for i in tilesInner:
            # print(f"xIDX: {xIDX}")
            # print(f"yIDX: {yIDX}")
            # print(f"ErgPic: {ergPic}")
            if ergPic[xIDX - 1, yIDX] in tilesMatches[i] and ergPic[xIDX, yIDX - 1] in tilesMatches[i]:
                ergPic[xIDX, yIDX] = i
                found = True
                break
        if found:
            tilesInner.remove (i)
        else:
            print(f"Error - not found something for postion X/Y {xIDX,yIDX}")

print(ergPic)
print(f"Corner Tiles: {len(tilesCorners), tilesCorners}")
print(f"Edge Tiles: {len(tilesEdges), tilesEdges}")
tilesInner.sort()
print(f"Inner Tiles: {len(tilesInner), tilesInner}")
for yIDX in range (widthOfPic):
    line = ""
    for xIDX in range(widthOfPic):
        line = line + " " + ergPic[(xIDX,yIDX)]
    print(line)

# print picture
for yIDX in range (widthOfPic):
    for linePic in range (10):
        line = ""
        for xIDX in range(widthOfPic):
            line = line + "   " + tilesDict[ergPic[(xIDX,yIDX)]][linePic]
        print (line)
    print("\n")

for key,val in tilesDict.items():
    print(key,val)
for key,val in tilesDictEdge.items():
    print(key,val)

arrangeTile(tile1, tile2, tileEdge1, tileEdge2, matchSide, tile3=0, tileEdge3=0):

