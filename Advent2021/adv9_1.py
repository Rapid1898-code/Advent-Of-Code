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

sumErg = 0
for Y,wRow in enumerate(listInp):
  for X,wChar in enumerate(wRow):
    if checkLow(listInp,X,Y):
      sumErg += int(listInp[Y][X]) + 1
    # print(f"Y: {Y}")
    # print(f"X: {X}")
    # print(listInp[Y][X])
    # print(sumErg)
    # input()

print(sumErg)

