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
# print(wY, wX)
# print(listObstacles)
# print(listPositions)
# exit()

listPositions = [(wY,wX)]
while True:
  if wDir == "U":
    wY -= 1
    if wY < 0:
      break
    if (wY,wX) in listObstacles:
      wDir = "R"
      wY += 1
      continue
    if (wY,wX) not in listPositions:
      listPositions.append((wY,wX))
  elif wDir == "D":
    wY += 1
    if wY == len(lines):
      break
    if (wY,wX) in listObstacles:
      wDir = "L"
      wY -= 1      
      continue      
    if (wY,wX) not in listPositions:
      listPositions.append((wY,wX))
  elif wDir == "R":
    wX += 1
    if wX == len(lines[0]):
      break
    if (wY,wX) in listObstacles:
      wDir = "D"
      wX -= 1
      continue      
    if (wY,wX) not in listPositions:
      listPositions.append((wY,wX))
  elif wDir == "L":
    wX -= 1
    if wX < 0:
      break
    if (wY,wX) in listObstacles:
      wDir = "U"
      wX += 1
      continue      
    if (wY,wX) not in listPositions:
      listPositions.append((wY,wX))

  # print(len(listPositions))
  # print(wDir)
  # print(listPositions)
  # input("Press!")


print(len(listPositions))  