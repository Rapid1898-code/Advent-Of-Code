import statistics

with open("adv7.txt","r") as f:
  listInp = [x.strip() for x in f.readlines()]
listInp = listInp[0].split(',')
listInp = [int(x) for x in listInp]

meanVal = statistics.mean(listInp)
stdevVal = statistics.stdev(listInp)

checkPos = list(set(listInp))
checkPosFin = []
for ePos in checkPos:
  if ePos < meanVal and ePos + stdevVal >= meanVal \
     or ePos > meanVal and ePos - stdevVal <= meanVal:    
    checkPosFin.append(ePos)

print(listInp)
print(checkPosFin)

countMin = 9999999
for ePos in checkPosFin:
  tmpCount = 0
  for eInp in listInp:
    if eInp >= ePos:
      tmpCount += eInp - ePos
    else:
      tmpCount += ePos - eInp
    if tmpCount > countMin:
      break
  if tmpCount < countMin:
    countMin = tmpCount

print(countMin)











    
