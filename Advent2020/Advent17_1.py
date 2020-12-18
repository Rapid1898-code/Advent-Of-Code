import copy

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

cubes = {}
tempcubes = {}
inpTmp = readInput("Advent17.txt",mode=0)
inpList = list(map(list, inpTmp))
# print(inpTmp)
# print(inpList)

cubes[-1] = [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]
# cubes[-1] = inpList
cubes[0] = inpList
cubes[1] = [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]
# cubes[1] = inpList
print(cubes)
dimension = [-1,0,1]
tempcubes = copy.deepcopy(cubes)


for idxZ in dimension:
    for idxY in range(len(cubes[0])):
        for idxX in range (len (cubes[0])):
            # count neighbours e.g. coordinate 0, 0, -1
            active = 0

            # check middle block
            if idxZ > dimension[0]:
                if cubes[idxZ-1][idxY][idxX] == "#": active += 1
            if idxZ < dimension[-1]:
                if cubes[idxZ+1][idxY][idxX] == "#": active += 1

            #check down
            if idxY < len(cubes[0])-1:
                if cubes[idxZ][idxY+1][idxX] == "#": active +=1
                if idxZ > dimension[0]:
                    if cubes[idxZ-1][idxY+1][idxX] == "#": active += 1
                if idxZ < dimension[-1]:
                    if cubes[idxZ+1][idxY+1][idxX] == "#": active += 1

            #check left-down
            if idxY < len (cubes[0]) - 1 and idxX > 0:
                if cubes[idxZ][idxY+1][idxX-1] == "#": active +=1
                if idxZ > dimension[0]:
                    if cubes[idxZ-1][idxY+1][idxX-1] == "#": active += 1
                if idxZ < dimension[-1]:
                    if cubes[idxZ+1][idxY+1][idxX-1] == "#": active += 1

            #check right-down
            if (idxY < len (cubes[0]) - 1) and (idxX < len (cubes[0]) - 1):
                # print(f"Len: {len(cubes[0])}")
                # print(f"IDX: {idxX}")
                # print(f"IDY: {idxY}")
                # print(f"Cubes: {cubes[-1]}")
                if cubes[idxZ][idxY+1][idxX+1] == "#": active +=1
                if idxZ > dimension[0]:
                    if cubes[idxZ-1][idxY+1][idxX+1] == "#": active += 1
                if idxZ < dimension[-1]:
                    if cubes[idxZ+1][idxY+1][idxX+1] == "#": active += 1

            #check left
            if idxX > 0:
                if cubes[idxZ][idxY][idxX-1] == "#": active +=1
                if idxZ > dimension[0]:
                    if cubes[idxZ-1][idxY][idxX-1] == "#": active += 1
                if idxZ < dimension[-1]:
                    if cubes[idxZ+1][idxY][idxX-1] == "#": active += 1

            #check right
            if idxX < len(cubes[0])-1:
                if cubes[idxZ][idxY][idxX+1] == "#": active +=1
                if idxZ > dimension[0]:
                    if cubes[idxZ-1][idxY][idxX+1] == "#": active += 1
                if idxZ < dimension[-1]:
                    if cubes[idxZ+1][idxY][idxX+1] == "#": active += 1

            #check up
            if idxY > 0:
                # print(f"Check: Z:{-1}, X:{idxX}, Y:{idxY} ")
                if cubes[idxZ][idxY-1][idxX] == "#": active +=1
                if idxZ > dimension[0]:
                    if cubes[idxZ-1][idxY-1][idxX] == "#": active += 1
                if idxZ < dimension[-1]:
                    if cubes[idxZ+1][idxY-1][idxX] == "#": active += 1

            #check left-up
            if idxY > 0 and idxX > 0:
                if cubes[idxZ][idxY-1][idxX-1] == "#": active +=1
                if idxZ > dimension[0]:
                    if cubes[idxZ-1][idxY-1][idxX-1] == "#": active += 1
                if idxZ < dimension[-1]:
                    if cubes[idxZ+1][idxY-1][idxX-1] == "#": active += 1

            #check right-up
            if (idxY < len (cubes[0]) - 1) and (idxX < len (cubes[0]) - 1):
                if cubes[idxZ][idxY+1][idxX+1] == "#": active +=1
                if idxZ > dimension[0]:
                    if cubes[idxZ-1][idxY+1][idxX+1] == "#": active += 1
                if idxZ < dimension[-1]:
                    if cubes[idxZ+1][idxY+1][idxX+1] == "#": active += 1

            print(f"Check: Z:{-1}, X:{idxX}, Y:{idxY}, Active: {active} ")

            if cubes[idxZ][idxY][idxX] == "#":
                if active < 2 or active > 3:
                    tempcubes[idxZ][idxY][idxX] = "."
            elif cubes[idxZ][idxY][idxX] == ".":
                if active == 3:
                    tempcubes[idxZ][idxY][idxX] = "#"
            else:
                print(f"Error - wrong char: {cubes[idxZ][idxY][idxX]}")

for key, val in cubes.items():
    print(key,val)
for key, val in tempcubes.items():
    print(key,val)





