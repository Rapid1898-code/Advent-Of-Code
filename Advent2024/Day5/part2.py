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
  if not checkFlag:
    print(wProtocol)
    while True:
      for idx, checkElem in enumerate(wProtocol):
        checkIDX = idx + 1
        if checkElem not in dictRules:
          newProtocol = wProtocol[:]
          newProtocol.pop(idx)
          newProtocol.append(checkElem)
          break
        if wProtocol[checkIDX] not in dictRules[checkElem]:
          newProtocol = wProtocol[:]
          newProtocol[idx] = wProtocol[checkIDX]
          newProtocol[checkIDX] = wProtocol[idx]
          break
        
      checkFlag = checkProtocol(newProtocol)                
      
      # print(f"Initial: {wProtocol}")
      # print(newProtocol)
      # print(checkFlag)
      # input("Press")

      if checkFlag:
        idxResult = int(abs(len(newProtocol) / 2))
        middleNumber = int(newProtocol[idxResult])
        sumErg += middleNumber
        break
      else:
        wProtocol = newProtocol[:]
      










print(sumErg)