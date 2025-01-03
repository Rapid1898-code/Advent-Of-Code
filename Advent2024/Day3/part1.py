import os 
import sys
import re


path = os.path.abspath(os.path.dirname(sys.argv[0])) 
fn = os.path.join(path, "inp.txt")
with open(fn, encoding="utf8", errors="ignore") as f:
  lines = f.read().splitlines()
baseString = lines[0]

idxList = [x.start() for x in re.finditer("mul", baseString)]
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
