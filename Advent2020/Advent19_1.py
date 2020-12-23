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
        rulesNr = int(elem.split(": ")[0])
        tmpRuleCont = list(elem.split(": ")[1].split(" "))
        for i in tmpRuleCont:
            if i != " " and i != '"':
                if i not in ["|",'"a"','"b"']:
                    rulesCont.append(int(i))
                elif i == "|":
                    rulesCont.append (i)
                elif i == '"a"':
                    rulesCont.append ("a")
                elif i == '"b"':
                    rulesCont.append ("b")
        rulesDict[rulesNr] = rulesCont
    elif part == 1:
        messagesList.append(elem)

rulesDict = {k: v for k, v in sorted(rulesDict.items(),
         key=lambda item: item[0])}

for key,val in rulesDict.items():
    print(key,val)
print(messagesList)

longMessage = 0
for i in messagesList:
    if len(i) > longMessage:
        longMessage = len(i)
print(f"Long Message: {longMessage}")

searchRules = [rulesDict[0]]
print(f"SearchRules Start: {searchRules}")
endRun = False

ergList = []
while not endRun:
    endRun = True
    # print (f"SearchRules During: {searchRules}")
    print(f"SearchRules: {len(searchRules)}")
    print(f"ErgList: {len(ergList)}")
    # if len(ergList) > 150000:
    #     break
    # input()

    for idx, listElements in enumerate(searchRules):
        # e.g. [8, 1, 1]
        countAB = 0
        onlyAB = True
        for i in listElements:
            if i in ["a","b"]:
                countAB +=1
                if countAB > longMessage:
                    break
            else:
                onlyAB = False
                break

        if onlyAB:
            # print(listElements)
            # print(f"IDX: {idx}")
            ergList.append(listElements)
            del searchRules[idx]
            endRun = False
            break

        for elemIDX, elemCont in enumerate (listElements):
            # print("DEBUG:",elemIDX,elemCont)
            # print("DEBUG2: ",rulesDict[elemCont])
            # input()

            if elemCont not in ["a","b"]:
                if "|" in rulesDict[elemCont]:
                    newListElements = listElements.copy ()
                    part = 0
                    tempLeft = []
                    tempRight = []
                    for tmpElm in rulesDict[elemCont]:
                        if tmpElm == "|":
                            part = 1
                        elif part == 0:
                            tempLeft.append(tmpElm)
                        elif part == 1:
                            tempRight.append(tmpElm)
                    del listElements[elemIDX]
                    for tmpElm in reversed(tempLeft):
                        listElements.insert (elemIDX, tmpElm)

                    del newListElements[elemIDX]
                    for tmpElm in reversed(tempRight):
                        newListElements.insert (elemIDX, tmpElm)
                    searchRules.append(newListElements)
                    endRun = False
                    break

                # print(rulesDict[elemCont])
                if rulesDict[elemCont][0] in ["a","b"]:
                    del listElements[elemIDX]
                    listElements.insert (elemIDX, rulesDict[elemCont][0])
                    endRun = False
                    break
                else:
                    del listElements[elemIDX]
                    for tmpElm in reversed(rulesDict[elemCont]):
                        listElements.insert (elemIDX, tmpElm)
                    endRun = False
                    break
        if not endRun:
            break

print (f"SearchRules End: {searchRules}")
for elemIDX, elemCont in enumerate(searchRules):
    searchRules[elemIDX] = "".join(elemCont)
print(f"Converted to String: {searchRules}")

for ergIDX, ergCont in enumerate(ergList):
    ergList[ergIDX] = "".join(ergCont)
print(f"Converted to String ERG: {ergList}")

# lenString = len(searchRules[0])
countMessages = 0
for elem in messagesList:
    if elem in ergList:
        print(f"{elem}")
        countMessages += 1

print(f"Matched Message: {countMessages}")



