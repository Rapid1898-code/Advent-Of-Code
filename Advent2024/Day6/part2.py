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

finalOut = []
for idx, e in enumerate(listObstacles):  
  workIDX = idx + 1
  foundElemsList = []

  while workIDX < len(listObstacles):
    if listObstacles[workIDX][0] == e[0] + 1:
      foundElemsList.append(listObstacles[workIDX])
    workIDX += 1
  for e2 in foundElemsList:
    workIDX = idx + 1    
    while workIDX < len(listObstacles):

      # print(e, e2)
      # print(workIDX)
      # print(listObstacles[workIDX])
      # print(finalOut)
      # input("Press1")

      if listObstacles[workIDX][1] == e2[1] - 1:
        # print(e, e2, listObstacles[workIDX])
        # input("Press!")
        finalOut.append((e, e2, listObstacles[workIDX]))                        
      workIDX += 1    

  while workIDX < len(listObstacles):
    if listObstacles[workIDX][1] == e[1] + 1:

      # print(listObstacles[workIDX])
      # input("Press!")


      foundElemsList.append(listObstacles[workIDX])
    workIDX += 1

  for e2 in foundElemsList:
    workIDX = idx + 1    
    while workIDX < len(listObstacles):

      # print(e, e2)
      # print(workIDX)
      # print(listObstacles[workIDX])
      # print(finalOut)
      # input("Press1")

      if listObstacles[workIDX][0] == e2[0] - 1:
        # print(e, e2, listObstacles[workIDX])
        # input("Press!")
        finalOut.append((e, e2, listObstacles[workIDX]))                        
      workIDX += 1    





print(finalOut)

      

