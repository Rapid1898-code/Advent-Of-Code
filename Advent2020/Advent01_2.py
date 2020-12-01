import itertools

def readInput(fn,makeInt=False):
    with open (fn, "r") as f:
        listInp = [x.strip () for x in f.readlines ()]
    if makeInt: listInp = [int (x) for x in listInp]
    return(listInp)

def adv1 (listInp):
    for i in itertools.combinations (listInp, 3):
        erg = i[0] + i[1] + i[2]
        if erg == 2020:
            return(i[0] * i[1] * i[2])


listInp = readInput("Advent01.txt",makeInt=True)
print(adv1(listInp))
