def readInput(fn,makeInt=False):
    with open (fn, "r") as f:
        listInp = [x.strip () for x in f.readlines ()]
    if makeInt: listInp = [int (x) for x in listInp]
    return(listInp)

inpList = readInput("Advent05.txt")

seatedPlaces = []
highestPass = 0
for ticket in inpList:
    rows = ticket[:7]
    cols = ticket[7:]
    rowStart = 0
    rowEnd = 128
    for idx in range (7):
        if rows[idx] == "F":
            rowEnd -= (rowEnd-rowStart) / 2
        elif rows[idx] == "B":
            rowStart += (rowEnd-rowStart) / 2
        else:
            print(f"ERROR - No B or F...")
    rowEnd = int(rowStart)
    
    colStart = 0
    colEnd = 8
    for idx in range(3):
        if cols[idx] == "L":
            colEnd -= (colEnd-colStart) / 2
        elif cols[idx] == "R":
            colStart += (colEnd-colStart) / 2
        else:
            print(f"ERROR - No B or F...")
    colEnd = int(colStart)
    seatID = int(rowEnd * 8 + colEnd)
    if seatID > highestPass: highestPass = seatID
    # print(f"Ticket {ticket}: SeatID: {seatID}, Row: {rowEnd}, Col: {colEnd}")
print(f"Highest PassID: {highestPass}")


