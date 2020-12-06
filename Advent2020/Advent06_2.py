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

inpList = readInput("Advent06.txt",mode=2)
# print(inpList)

countAnswers = 0
for group in inpList:
    for idx, answer in enumerate(group):
        if idx == 0: tmpSet = set (answer)
        tmpSet = tmpSet & set(answer)
    print(f"Group {group} with {len(tmpSet)} answers")
    countAnswers += len(tmpSet)

print(f"Overall answers: {countAnswers}")





