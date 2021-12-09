with open("adv9.txt","r") as f:
  listInp = [x.strip() for x in f.readlines()]

def checkLow(listInp,X,Y):
  checkVal = int(listInp[Y][X])
  lenY = len(listInp) - 1
  lenX = len(listInp[0]) - 1
  low = True
  if (X > 0 and int(listInp[Y][X-1]) <= checkVal) \
    or (X < lenX and int(listInp[Y][X+1]) <= checkVal) \
    or (Y > 0 and int(listInp[Y-1][X]) <= checkVal) \
    or (Y < lenY and int(listInp[Y+1][X]) <= checkVal):
    return False
  else:
    return True

coordErg = []
for Y,wRow in enumerate(listInp):
  for X,wChar in enumerate(wRow):
    if checkLow(listInp,X,Y):
      coordErg.append([X,Y])
    # print(f"Y: {Y}")
    # print(f"X: {X}")
    # print(listInp[Y][X])
    # print(sumErg)
    # input()

lenY = len(listInp) - 1
lenX = len(listInp[0]) - 1
for X,Y in coordErg:
  print(f"Check X: {X}, Y: {Y}")
  horizLeft = horizRight = vertiUp = vertiDown = False
  
  # checkMaxPosLeft
  xCheck = [X]
  yCheck = [Y]

  horizLeft = X
  while True:
    if horizLeft > 0 and listInp[Y][horizLeft-1] != "9":
      horizLeft -= 1
      xCheck.append(horizLeft)
    else:
      break
 
  # checkMaxPosRight
  horizRight = X
  while True:
    if horizRight < lenX and listInp[Y][horizRight+1] != "9":
      horizRight += 1
      xCheck.append(horizRight)
    else:
      break

  # checkMaxPosUp
  vertiUp = Y
  while True:
    if vertiUp > 0 and listInp[vertiUp-1][X] != "9":
      vertiUp -= 1
      yCheck.append(vertiUp)
    else:
      break

  # checkMaxPosDown
  vertiDown = Y
  while True:
    if vertiDown < lenY and listInp[vertiDown+1][X] != "9":
      vertiDown += 1
      yCheck.append(vertiDown)
    else:
      break

  # print(f"HorizLeft: {horizLeft}")
  # print(f"HorizRight: {horizRight}")
  # print(f"VertiUp: {vertiUp}")
  # print(f"VertiDown: {vertiDown}")
  print(xCheck)
  print(yCheck)
  # exit()

  countTemp = 1
  for checkX in xCheck:
    vertiUp = Y
    while True:
      if vertiUp > 0 and listInp[vertiUp-1][checkX] != "9":
        vertiUp -= 1
        countTemp += 1
      else:
        break
    print(f"CheckVertiUp: {countTemp}")

    vertiDown = Y
    while True:
      if vertiDown < lenY and listInp[vertiDown+1][checkX] != "9":
        vertiDown += 1
        countTemp += 1
      else:
        break
    print(f"CheckVertiDown: {countTemp}")
  
  for checkY in yCheck:
    horizLeft = X
    while True:
      if horizLeft > 0 and listInp[checkY][horizLeft-1] != "9":
        horizLeft -= 1
        countTemp += 1
      else:
        break
    print(f"CheckHorizLeft: {countTemp}")

    horizRight = X
    while True:
      if horizRight < lenX and listInp[checkY][horizRight+1] != "9":
        horizRight += 1
        countTemp += 1
      else:
        break
    print(f"CheckHorizRight: {countTemp}")

  print(countTemp)
  input()







  


