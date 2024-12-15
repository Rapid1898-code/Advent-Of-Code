import os 
import sys
import string

path = os.path.abspath(os.path.dirname(sys.argv[0])) 
fn = os.path.join(path, "inp.txt")
with open(fn, encoding="utf8", errors="ignore") as f:
  lines = f.read().splitlines()

def checkProtocol(wProtocol): 
  for idx, checkElem in enumerate(wProtocol):
    checkIDX = idx + 1
    if checkIDX == len(wProtocol):
      return True
    while checkIDX < len(wProtocol):
      if checkElem not in dictRules or wProtocol[checkIDX] not in dictRules[checkElem]:
        checkFlag = False
        return False
      checkIDX += 1

dictRules = {}
listProtocol = []
sumErg = 0
for l in lines:
  if "|" in l:
    firstVal, secondVal = l.split("|")
    if firstVal not in dictRules:
      dictRules[firstVal] = [secondVal]
    else:
      dictRules[firstVal].append(secondVal)
  if "," in l:
    listProtocol.append(l.split(","))

for wProtocol in listProtocol:
  
  checkFlag = checkProtocol(wProtocol)      
  if checkFlag:
    idx = int(abs(len(wProtocol) / 2))
    middleNumber = int(wProtocol[idx])
    sumErg += middleNumber
print(sumErg)








