import math
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

def calcLCM(a, b):
    return abs(a*b) // math.gcd(a, b)

inpList = readInput("Advent13.txt",mode=0)
target = int(inpList[0])
times = inpList[1].split(",")
timesDiff = []
for idx,cont in enumerate(times):
    if cont == "x":
        continue
    else:
        timesDiff.append((int(cont),idx))
print(timesDiff)

listDiffs = []
listDiffDetails = []
bigDiff = bigStart = 0
for i in timesDiff[1:]:
    # print(i)
    n1 = timesDiff[0][0]
    n2 = i[0]
    finalStart = 0
    finalDiff = 0
    start = 0
    while True:
        start += n1
        if (start + i[1]) % n2 == 0:
            if finalStart == 0:
                finalStart = start
            else:
                finalDiff = start - finalStart
        if finalStart != 0 and finalDiff != 0:
            break
    listDiffs.append(start)
    if finalDiff > bigDiff:
        bigDiff = finalDiff
        bigStart = finalStart
    listDiffDetails.append((i,finalStart,finalDiff))
# print(listDiffs)
for i in listDiffDetails:
    print(i)

print(f"BigStart: {bigStart}, Bigdiff: {bigDiff}")

start = bigStart + 116000000000000
# start = bigStart
while True:
    start += bigDiff
    erg = True
    # for i in listDiffDetails[:4]:
    for i in listDiffDetails:
        # print(f"{start}, {i[2]}, {i[1]}, {start % i[2]}")
        # input()
        if start % i[2] != i[1]:
            erg = False
            break
    if erg:
        break
    print(start)

print(f"Final: {start}")





#
# n1 = 7
# n2 = 59
# start = 602
#
# while True:
#     start += n1
#     end = False
#     if start % n2 == 5:
#         end = True
#         break
#
# print(start)



