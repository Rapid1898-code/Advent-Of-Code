import statistics

with open("adv7.txt","r") as f:
  listInp = [x.strip() for x in f.readlines()]
listInp = listInp[0].split(',')
listInp = [int(x) for x in listInp]

tmpDict = {}
actVal = 0
for i in range(1,1900):
  actVal += i
  tmpDict[i] = actVal

meanVal = statistics.mean(listInp)
stdevVal = statistics.stdev(listInp)

checkPos = list(set(listInp))
checkPosFin = []
for ePos in checkPos:
  if ePos < meanVal and ePos + stdevVal >= meanVal \
     or ePos > meanVal and ePos - stdevVal <= meanVal:    
    checkPosFin.append(ePos)
minPos = min(checkPosFin)
maxPos = max(checkPosFin)
for i in range(minPos, maxPos+1):
  if i not in (checkPosFin):
    checkPosFin.append(i)

print(listInp)
print(checkPosFin)

countMin = 9999999999999
for ePos in checkPosFin:
  tmpCount = 0
  for eInp in listInp:
    if eInp >= ePos:
      diff = eInp - ePos
      if diff != 0:
        tmpCount += tmpDict[diff]
    else:
      diff = ePos - eInp
      if diff != 0:
        tmpCount += tmpDict[diff]        
    
    # if ePos == 5:
    #   print(eInp)
    #   print(diff)
    #   print(tmpDict[diff])
    #   input()
    
    if tmpCount > countMin:
      break
  if tmpCount < countMin:
    countMin = tmpCount

print(countMin)











    
