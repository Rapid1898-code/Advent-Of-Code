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

inpTmp = readInput("Advent22.txt",mode=0)
print(inpTmp)

deckPlayer1 = []
deckPlayer2 = []
part = 0
for elem in inpTmp:
    if "Player" in elem:
        continue
    if elem == "":
        part = 1
        continue
    if part == 0:
        deckPlayer1.append(int(elem))
    if part == 1:
        deckPlayer2.append(int(elem))
# print (f"Player1: {deckPlayer1}")
# print (f"Player2: {deckPlayer2}")

round = 1
while deckPlayer1 != [] and deckPlayer2 != []:
    print(f"Round {round}")
    print(f"Player1: {deckPlayer1}")
    print(f"Player2: {deckPlayer2}")
    # input("Press <Enter> to continue...")
    cardPlayer1 = deckPlayer1[0]
    cardPlayer2 = deckPlayer2[0]
    if cardPlayer1 > cardPlayer2:
        deckPlayer1.extend([cardPlayer1,cardPlayer2])
        deckPlayer1.pop(0)
        deckPlayer2.pop(0)
    elif cardPlayer2 > cardPlayer1:
        deckPlayer2.extend([cardPlayer2,cardPlayer1])
        deckPlayer1.pop(0)
        deckPlayer2.pop(0)
    else:
        print(f"Error - Cards Are Identical! {cardPlayer1}, {cardPlayer2}")
        input()
    round += 1

deckWin = []
if deckPlayer1 == []:
    print(f"Winner is Player2")
    deckWin = deckPlayer2.copy()
elif deckPlayer2 == []:
    print(f"Winner is Player1")
    deckWin = deckPlayer1.copy()
print(f"WinnerDeck: {deckWin}")

winningScore = 0
for idx in range(len(deckWin), 0, -1):
    idxDeck = abs(idx-len(deckWin))
    winningScore += (deckWin[idxDeck] * idx)
print(f"WinningScore: {winningScore}")





