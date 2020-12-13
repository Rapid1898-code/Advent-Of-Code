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

inpList = readInput("Advent13.txt",mode=0)
target = int(inpList[0])
times = inpList[1].split(",")
for idx,cont in enumerate(times):
    if cont != "x": times[idx] = int(times[idx])
print(target)
print(times)

minWait = busnr = 99999999
for bus in times:
    if bus == "x":
        continue
    diff = target // bus
    nextStart = diff * bus + bus
    wait = nextStart - target
    if wait < minWait:
        minWait = wait
        busNr = bus
    # print(diff)
    # print(nextStart)
    # print(wait)

print(f"BusNr: {busNr}")
print(f"MinWait: {minWait}")
print(f"Multiplication BusNr * MinWait: {busNr * minWait}")

