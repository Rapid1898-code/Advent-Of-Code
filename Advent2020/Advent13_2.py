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

tmperg = 149669104223100 // timesDiff[0][0]
timeCheck = tmperg * timesDiff[0][0]

while True:
    timeCheck += timesDiff[0][0]
    found = True
    for checkElem in timesDiff[1:]:
        if checkElem[0] - (timeCheck % checkElem[0]) != checkElem[1]:
            found = False
            break
    if found: break
    print(timeCheck)
print(timeCheck)

# lcm = timesDiff[0][0]
# for i in timesDiff[1:]:
#     if i == "x":
#         continue
#     lcm = calcLCM(lcm, i[0]+i[1])
#
# print(f"Earliest Timestamp: {lcm}")








