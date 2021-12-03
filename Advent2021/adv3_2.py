with open("adv3.txt","r") as f:
  listInp = [x.strip() for x in f.readlines()]

def checkMost (listCheck, pos, greater):
  countZero = countOne = 0
  for e in listCheck:
    if e[pos] == "0":
      countZero += 1
    else:
      countOne += 1
  if greater == True:
    if countZero > countOne:
      return 0
    else:
      return 1
  else:
    if countZero <= countOne:
      return 0
    else:
      return 1

workList = listInp[:]
for i in range(len(listInp[0])):
  if len(workList) == 1:
    break
  mostBit = str(checkMost(workList,i,True))
  for idx in range(len(workList)-1,-1,-1):
    if workList[idx][i] != mostBit:
      del(workList[idx])
erg1 = int(workList[0],2)
print(erg1)

workList = listInp[:]
for i in range(len(listInp[0])):
  if len(workList) == 1:
    break
  mostBit = str(checkMost(workList,i,False))
  for idx in range(len(workList)-1,-1,-1):
    if workList[idx][i] != mostBit:
      del(workList[idx])
erg2 = int(workList[0],2)
print(erg2)
print(erg1*erg2)






