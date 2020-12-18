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

inpList = readInput("Advent18.txt",mode=0)

def calcMultiplication(expression):
    while "+" in expression or "*" in expression:
        firstNum = -1
        for idxChar, Char in enumerate(expression):
            if Char in ["+","*"] and firstNum == -1:
                firstNum = int(expression[:idxChar].strip())
                expressionChar = Char
                expressionPos = idxChar + 1
            elif (Char in ["+","*"] and firstNum != -1) or (idxChar == len(expression) -1):

                # print(f"\nActualExpression: {expression}")
                # print(f"IDX Char: {idxChar}")
                # print(f"Len Expression: {len(expression)}")
                # print(f"FirstNum: {firstNum}")
                # print(f"ExpressionChar: {expressionChar}")
                # print(f"ExpressionPos: {expressionPos}")
                # print(f"SecondNum: {expression[expressionPos:idxChar].strip()}")
                # print(f"Rest of Expression: {expression[expressionPos:]}")

                if idxChar < len(expression) -1:
                    secondNum = int(expression[expressionPos:idxChar].strip())
                elif idxChar == len(expression) -1:
                    secondNum = int (expression[expressionPos:].strip ())

                if expressionChar == "+":
                    tmpErg = firstNum + secondNum
                elif expressionChar == "*":
                    tmpErg = firstNum * secondNum
                else:
                    print(f"Error - Wrong ExpressionChar: {expressionChar}")

                if idxChar < len(expression) -1:
                    expression = str(tmpErg) + " " + expression[idxChar:]
                elif idxChar == len(expression) -1:
                    expression = str(tmpErg)
                break
    return(int(expression))

def calcAddition(expression):
    while "+" in expression:
        # print(f"\nExpression Before: {expression}")
        posFirstDigit = -1
        posExpression = -1
        posLastDigit = -1
        firstNum = -1
        secondNum = -1
        for idxChar, Char in enumerate(expression):

            print (f"\nActualExpression: {expression}")
            print (f"IDX Char: {idxChar}")
            print (f"Len Expression: {len (expression)}")
            print (f"FirstNum: {firstNum}")
            print (f"PosFirstDigit: {posFirstDigit}")
            print (f"PosExpression: {posExpression}")
            print (f"PosLastDigit: {posLastDigit}")
            print (f"SecondNum: {secondNum}")
            print (f"Rest of Expression: {expression[posLastDigit:]}")

            if Char.isdigit() and posFirstDigit == -1:
                posFirstDigit = idxChar
                continue
            if Char == "*" and posExpression == -1:
                posFirstDigit = -1
                continue
            if Char == "+" and posExpression == -1:
                posExpression = idxChar
                firstNum = int(expression[posFirstDigit:posExpression].strip())
                continue
            if (not Char.isdigit() and Char != " " and posExpression != -1) or idxChar == len(expression) - 1:
                posLastDigit = idxChar
                if idxChar < len (expression) - 1:
                    secondNum = int(expression[posExpression + 1:posLastDigit].strip())
                elif idxChar == len (expression) - 1:
                    secondNum = int (expression[posExpression + 1:].strip ())
                tmpErg = firstNum + secondNum
                if idxChar < len (expression) - 1:
                    expression = expression[:posFirstDigit] + " " + str(tmpErg) + " " + expression[posLastDigit:]
                elif idxChar == len (expression) - 1:
                    expression = expression[:posFirstDigit] + " " + str(tmpErg)
                break
        # print (f"Expression After: {expression}")

        # input()

    return(expression)

# tst = "1 + 2 * 3 + 4 * 5 + 6"
# tstStr = calcAddition(tst)
# tstStr = calcMultiplication(tstStr)
# print(f"Final: {tstStr}")

sumErg = 0
for expression in inpList:
    while "(" in expression:
        # print(f"Expression Before: {expression}")
        for idxChar, Char in enumerate(expression):
            if Char == "(":
                posOpenBracket = idxChar
            if Char == ")":
                posEndBracket = idxChar
                tmpErg = calcAddition(expression[posOpenBracket + 1:posEndBracket])
                tmpErg = calcMultiplication(tmpErg)
                expression = expression[:posOpenBracket] + " " + str(tmpErg) + " " + expression[posEndBracket+1:]
                break
        # print (f"Expression After: {expression}")
    erg = calcAddition (expression)
    erg = calcMultiplication(erg)
    sumErg += erg

print(f"SumErg: {sumErg}")
