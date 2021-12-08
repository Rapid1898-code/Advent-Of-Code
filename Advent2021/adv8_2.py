import statistics

with open("adv8.txt","r") as f:
  listInp = [x.strip() for x in f.readlines()]
listInp = [[x.split(" | ")[0].split(), x.split(" | ")[1].split()] for x in listInp]

for i,e in enumerate(listInp):
  listInp[i][0] = ["".join(sorted(x)) for x in listInp[i][0]]
  listInp[i][1] = ["".join(sorted(x)) for x in listInp[i][1]]

listCountErg = []
for row in listInp: 
  workList = row[0]
  print(workList)
  ergDict = {}
  for i in range(len(workList)-1,-1,-1):
    if len(workList[i]) in [2,4,3,7]:
      if len(workList[i]) == 2:
        ergDict[1] = workList[i]
      elif len(workList[i]) == 4:
        ergDict[4] = workList[i]
      elif len(workList[i]) == 3:
        ergDict[7] = workList[i]
      elif len(workList[i]) == 7:
        ergDict[8] = workList[i]
      del(workList[i])
     
  for i in range(len(workList)-1,-1,-1):
    if len(workList[i]) == 5:
      tmpCheck = list(ergDict[1])
      check = True
      for c in tmpCheck:
        if c not in workList[i]:
          check = False
      if check:
        ergDict[3] = workList[i]
        del(workList[i])
        break

  for i in range(len(workList)-1,-1,-1):
    if len(workList[i]) == 6:
      tmpCheck = list(ergDict[1])
      if tmpCheck[0] in workList[i] and tmpCheck[1] not in workList[i] \
          or tmpCheck[1] in workList[i] and tmpCheck[0] not in workList[i]:
        ergDict[6] = workList[i]
        del(workList[i])
        break       
  
  breakOut = False
  for i in range(len(workList)-1,-1,-1):
    if len(workList[i]) == 6:
      tmpCheck = list(ergDict[4])                     
      for c in tmpCheck:
        if c not in workList[i]:
          ergDict[0] = workList[i]
          del(workList[i])          
          for i2,e2 in enumerate(workList):
            if len(e2) == 6:
              ergDict[9] = e2
              del(workList[i2])
              breakOut = True
              break
          if breakOut:
            break
      if breakOut:
        break      

  tmpCheck1 = list(ergDict[1])
  tmpCheck2 = list(ergDict[4])
  tmpCheck = []
  for c in tmpCheck2:
    if c not in ergDict[1]:
      tmpCheck.append(c)
  check = True
  for c in tmpCheck:
    if c not in workList[0]:
      check = False
  if check:
    ergDict[5] = workList[0]
    ergDict[2] = workList[1]
  else:
    ergDict[2] = workList[0]
    ergDict[5] = workList[1]

  ergDict = dict((y,x) for x,y in ergDict.items())
  # print(ergDict)

  ergString = ""
  for e in row[1]:
    ergString += str(ergDict[e])
  listCountErg.append(int(ergString))

print(listCountErg)
print(sum(listCountErg))


