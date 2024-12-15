import os 
import sys
import string

path = os.path.abspath(os.path.dirname(sys.argv[0])) 
fn = os.path.join(path, "inp.txt")
with open(fn, encoding="utf8", errors="ignore") as f:
  lines = f.read().splitlines()

listObstacles = []
wDir = "U"
for y,l in enumerate(lines):
  breakOut = False
  for x,e in enumerate(l):
    if e == "^":
      listPositions = [(y,x)]            
      wY = y
      wX = x
    if e == "#":
      listObstacles.append((y,x))
print(wY, wX)
print(listObstacles)
print(listPositions)
exit()

for idx, e in enumerate(listObstacles):
  workIDX = idx + 1
  while workIDX < len(lsitObstacles):
    if listObstacles[workIDX[0]] = 

