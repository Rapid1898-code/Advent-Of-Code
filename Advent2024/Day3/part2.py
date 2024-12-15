import os 
import sys
import re


path = os.path.abspath(os.path.dirname(sys.argv[0])) 
fn = os.path.join(path, "inp.txt")
with open(fn, encoding="utf8", errors="ignore") as f:
  lines = f.read().splitlines()
baseString = lines[0]

workList = [x.start() for x in re.finditer("mul", baseString)]
lDONT = [x.start() for x in re.finditer("don't()", baseString)]
worker = [x.start() for x in re.finditer("do()", baseString)]
lDO = []
for e in worker:
  if e not in lDONT:
    lDO.append(e)    

idxList = []
flagCount = True
for i in range(len(baseString)):
  if i in workList and flagCount:
    idxList.append(i)
  if i in lDONT:
    flagCount = False
  if i in lDO:
    flagCount = True

ergSum = 0
for checkIDX in idxList:
  workIDX = checkIDX + 3
  if baseString[workIDX] != "(":
    continue
  workIDX += 1
 
  num1 = ""
  while baseString[workIDX].isdigit():
    num1 += baseString[workIDX]
    workIDX +=1
  num1 = int(num1)
  
  if baseString[workIDX] != ",":
    continue
  workIDX += 1

  num2 = ""
  while baseString[workIDX].isdigit():
    num2 += baseString[workIDX]
    workIDX +=1
  num2 = int(num2)
  
  if baseString[workIDX] != ")":
    continue

  ergSum += num1 * num2

print(ergSum)
