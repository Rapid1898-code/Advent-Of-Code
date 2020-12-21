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

def findSides (tile):
    top = tile[0]
    bottom = tile[-1]
    left = ""
    right = ""
    for line in tile:
        left += line[0]
        right += line[-1]
    return(top, right, bottom, left)

tile1427 = ['###.##.#..', '.#..#.##..', '.#.##.#..#', '#.#.#.##.#', '....#...##', '...##..##.', '...#.#####', '.#.####.#.', '..#..###.#', '..##.#..#.']
tile2311 = ['..##.#..#.', '##..#.....', '#...##..#.', '####.#...#', '##.##.###.', '##...#.###', '.#.#.#..##', '..#....#..', '###...#.#.', '..###..###']
tile2473 = ['#....####.', '#..#.##...', '#.##..#...', '######.#.#', '.#...#.#.#', '.#########', '.###.#..#.', '########.#', '##...##.#.', '..###.#.#.']
tile1489 = ['##.#.#....', '..##...#..', '.##..##...', '..#...#...', '#####...#.', '#..#.#.#.#', '...#.#.#..', '##.#...##.', '..##.##.##', '###.##.#..']
tile2729 = ['...#.#.#.#', '####.#....', '..#.#.....', '....#..#.#', '.##..##.#.', '.#.####...', '####.#.#..', '##.####...', '##..#.##..', '#.##...##.']

edge1427 = ['###.##.#..', '..###.#.#.', '..##.#..#.', '#..#......', '..#.##.###', '.#.#.###..', '.#..#.##..', '......#..#']
edge2311 = ['..##.#..#.', '...#.##..#', '..###..###', '.#####..#.', '.#..#.##..', '#..##.#...', '###..###..', '.#..#####.']
edge2473 = ['#....####.', '...###.#..', '..###.#.#.', '####...##.', '.####....#', '..#.###...', '.#.#.###..', '.##...####']
edge1489 = ['##.#.#....', '.....#..#.', '###.##.#..', '#...##.#.#', '....#.#.##', '.#..#.....', '..#.##.###', '#.#.##...#']
edge2729 = ['...#.#.#.#', '#..#......', '#.##...##.', '.#....####', '#.#.#.#...', '......#..#', '.##...##.#', '####....#.']

# match1427_2311 = list(set(edge1427) & set(edge2311))
# match1427_2473 = list(set(edge1427) & set(edge2473))
# match1427_1489 = list(set(edge1427) & set(edge1489))
# match1427_2729 = list(set(edge1427) & set(edge2729))
# print(f"Match 1427_2311: {match1427_2311}")
# print(f"Match 1427_2473: {match1427_2473}")
# print(f"Match 1427_1489: {match1427_1489}")
# print(f"Match 1427_2729: {match1427_2729}")

def arrangeTile(tile1,tile2,tileEdge1,tileEdge2,matchSide):
    match = list(set(tileEdge1) & set(tileEdge2))
    if matchSide == "R":
        while findSides(tile1)[1] not in match:
            # print(f"Right Side: {findSides(tile1)[1]}")
            tile1 = rotateTileClockwise(tile1,90)
        print (f"Tile1: Found Right Side: {findSides (tile1)[1]}")
        print(f"Tile1: Found: {tile1}")

        while findSides(tile2)[3] not in match:
            # print(f"Right Side: {findSides(tile1)[3]}")
            tile2 = rotateTileClockwise(tile2,90)
        print (f"Tile1: Found Right Side: {findSides (tile2)[3]}")
        print(f"Tile1: Found: {tile2}")

    return(tile1,tile2)


tile1, tile2 = arrangeTile(tile1427,tile2473,edge1427,edge2473,"R")

for i in tile1:
    print(i)
print("\n")
for i in tile2:
    print(i)





