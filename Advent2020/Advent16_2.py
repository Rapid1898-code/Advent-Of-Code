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

inpTmp = readInput("Advent16.txt",mode=0)

textSpans = {}
textNr = {}
yourTicket = []
nearbyTicket = []

parseMode = 0
textPos = 0
for line in inpTmp:
    if line == "":
        parseMode += 1
        continue
    if parseMode == 0:
        textPos += 1
        text = line.split(": ")[0]
        tmpCont = line.split(": ")[1]
        tmpCont = tmpCont.split(" or ")
        fromTo1 = list(map(int,tmpCont[0].split("-")))
        fromTo2 = list(map(int,tmpCont[1].split("-")))
        textSpans[text] = [fromTo1,fromTo2]
        textNr[text] = textPos
        # print(textSpans)
    elif parseMode == 1:
        if line == "your ticket:":
            continue
        yourTicket = list(map(int,line.split(",")))
    elif parseMode == 2:
        if line == "nearby tickets:":
            continue
        nearbyTicket.append(list (map (int, line.split (","))))
# print(textNr)
# print(textSpans)
# print(yourTicket)
# print(nearbyTicket)

nearbyTicketNew = []

print(f"Len Nearby Tickets: {len(nearbyTicket)}")
for ticket in nearbyTicket:
    correctTicket = True
    for number in ticket:
        correctNumber = False
        for key, val in textSpans.items ():
            # print(f"Ticket: {ticket}")
            # print(f"Val1: {val[0]}")
            # print(f"Val2: {val[1]}")
            if (number >= val[0][0] and number <= val[0][1]) or (number >= val[1][0] and number <= val[1][1]):
                correctNumber = True
                break
        if not correctNumber:
            correctTicket = False
            break
    if correctTicket:
        nearbyTicketNew.append(ticket)
print(f"Len Nearby Tickets New: {len(nearbyTicketNew)}")

erg = {}
position = 1
for ticket in nearbyTicketNew:
    for textKey, textVal in textSpans.items ():

        print(f"\nTicket: {ticket}")
        print(f"Text: {textKey, textVal}")


        foundPos = True
        for ticketItem in ticket:
            if (ticketItem >= textVal[0][0] and ticketItem <= textVal[0][1]) or (ticketItem >= textVal[1][0] and ticketItem <= textVal[1][1]):
                continue
            else:
                foundPos = False
                break
        if foundPos:
            posYourTicket = textNr[textKey]
            erg[position] = textKey, yourTicket[posYourTicket-1]
            del textSpans[textKey]
            position += 1
            break

multiplication = 1
for key, val in erg.items ():
    print(key,val)
    if "departure" in val[0]:
        multiplication *= val[1]

print(f"Multiplication: {multiplication}")














