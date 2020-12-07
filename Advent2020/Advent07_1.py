def readInput(fn,mode=0):
    """
    :param fn: input filname
    :param mode: 0 normal working, 1 changed to int, 2 seperated input with empty lines
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
    if mode == 1:
        listInp = [int (x) for x in listInp]
    return(listInp)

inpList = readInput("Advent07.txt",mode=0)

bagDict = {}
for elem in inpList:
    bagKey = elem.split("contain")[0].replace("bags","").strip()
    tmpBagValues = elem.split("contain")[1].strip()
    bagValuesDict = {}
    for value in tmpBagValues.split(","):
        value = value.replace(".","").replace("bags","").replace("bag","").strip()
        bagValueName = value[1:].strip()
        bagValueAmount = value[0]
        if value[0] == "n":
            bagValuesDict["nothing"] = 0
        else:
            bagValuesDict[bagValueName] = int(bagValueAmount)
    bagDict[bagKey] = bagValuesDict

# for key, val in bagDict.items():
#     print(key, val)

# countGoldBag = 0
# for key, val in bagDict.items():
#     if "shiny gold" in val:
#         countGoldBag += 1
#         continue
#     for keyBagContent, valBagContent in val:
#         del val[keyBagContent]

round = 0
goldBags = []
# find Bag with GoldBag
while True:
    round += 1
    tmpGoldBag = goldBags.copy()
    for key, val in bagDict.items():
        if key in goldBags: continue
        addBag = False
        if "shiny gold" in val:
            addBag = True
        for goldies in goldBags:
            if goldies in val:
                addBag = True
        if addBag:
            goldBags.append(key)

    print(f"Round: {round}")
    print(f"GoldBags: {goldBags}")
    print(f"TMPGoldBag: {tmpGoldBag}")

    if goldBags == tmpGoldBag:
        break
print(len(goldBags))









