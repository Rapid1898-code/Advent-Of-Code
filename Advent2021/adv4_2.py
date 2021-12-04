with open("adv4.txt","r") as f:
  listInp = [x.strip() for x in f.readlines()]

boards = []
tmpboard = []
finVal = []
for i,e in enumerate(listInp):
  if i == 0:
    numbers = e.split(",")
    numbers = [int(x) for x in numbers]
    continue
  if i == 1:
    continue
  if len(e) == 0:
    boards.append(tmpboard)
    finVal.append([])
    tmpboard = []
    continue
  row = e.split()
  row = [int(x) for x in row]
  tmpboard.append(row)
boards.append(tmpboard)
finVal.append([])

# check if board is finished (horizontal or vertical)
def checkBoard(board):
  for row in board:
    if sum(row) == -5:
      return True
  for colIdx in range(len(board[0])):
    checkCol = True
    for row in board:
      if row[colIdx] != -1:
        checkCol = False
        break
    if checkCol:
      return True
  return False

# update board and finished values for specific number
def updateBoard(board,finVal,nr):
  for idxRow, row in enumerate(board):
    for idxCell, cell in enumerate(row):
      # print(cell)
      # print(nr)
      if cell == nr:       
        finVal.append(cell)
        board[idxRow][idxCell] = -1         
        return board,finVal
  return board,finVal

finalNr = False
for idxNr, nr in enumerate(numbers):
  delIdxBoards = []
  for idxB, b in enumerate(boards):
    # print(boards[idxB])
    # print(finVal[idxB])
    # print(nr)
    boards[idxB], finVal[idxB] = updateBoard(boards[idxB], finVal[idxB], nr)          
    # print(idxB)
    # print(boards[idxB])
    # print(finVal[idxB])
    # input()
    if checkBoard(boards[idxB]):
      delIdxBoards.append(idxB)
  
  delIdxBoards.reverse()
  for idxDel in delIdxBoards:
    if len(boards) > 1:
      del boards[idxDel]        
      continue
    if len(boards) == 1:
      finalNr = nr
      finalIdxBoard = idxB
      break
  if finalNr:
    break

sumLeftNums = 0
for row in boards[0]:
  for cell in row:
    if cell != -1:
      sumLeftNums += cell

print(sumLeftNums)
print(finalNr)

erg = sumLeftNums * finalNr
print(erg)          





      















# actIdx = 0
# drawNum = 5
# drawRound = []
# while True:
#   if actIdx + drawNum > len(numbers):
#     drawRound.append(numbers[actIdx:])
#     break
#   actDraw = numbers[actIdx:actIdx + drawNum]
#   drawRound.append(actDraw)
#   actIdx += drawNum
#   drawNum += 1
# print(drawRound)






















