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

inpTmp = readInput("Advent19.txt",mode=0)
# print(inpTmp)

rulesDict = {}
messagesList = []
part = 0
for elem in inpTmp:
    if elem == "":
        part = 1
        continue
    if part == 0:
        rulesCont = []
        rulesNr = elem.split(": ")[0]
        tmpRuleCont = list(elem.split(": ")[1])
        for i in tmpRuleCont:
            if i != " " and i != '"':
                if i not in ["|","a","b"]:
                    rulesCont.append(int(i))
                else:
                    rulesCont.append (i)
        rulesDict[int(rulesNr)] = rulesCont
    elif part == 1:
        messagesList.append(elem)
print(rulesDict)
print(messagesList)

searchRules = [rulesDict[0]]
print(f"SearchRules Start: {searchRules}")
endRun = False
while not endRun:
    endRun = True
    print (f"SearchRules During: {searchRules}")
    for listElements in searchRules:
        for elemIDX, elemCont in enumerate (listElements):
            if elemCont not in ["a","b"]:
                if "|" in rulesDict[elemCont]:
                    newListElements = listElements.copy ()
                    listElements.insert (elemIDX, rulesDict[elemCont][1])
                    listElements.insert (elemIDX, rulesDict[elemCont][0])
                    del listElements[elemIDX+2]
                    newListElements.insert (elemIDX, rulesDict[elemCont][4])
                    newListElements.insert (elemIDX, rulesDict[elemCont][3])
                    del newListElements[elemIDX+2]
                    searchRules.append(newListElements)
                    endRun = False
                    break

                # print(rulesDict[elemCont])
                if rulesDict[elemCont][0] in ["a","b"]:
                    listElements[elemIDX] = rulesDict[elemCont][0]
        if not endRun:
            break

print (f"SearchRules End: {searchRules}")
for elemIDX, elemCont in enumerate(searchRules):
    searchRules[elemIDX] = "".join(elemCont)
print(f"Converted to String: {searchRules}")

lenString = len(searchRules[0])
countMessages = 0
for elem in messagesList:
    if elem in searchRules:
        print(f"{elem}")
        countMessages += 1
print(f"Matched Message: {countMessages}")



