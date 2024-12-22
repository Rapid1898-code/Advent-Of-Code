import os 
import sys
import string
from itertools import combinations

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

workCombis = list(combinations(listObstacles, 3))
print(f"Working for {len(workCombis)} combinations")

finalOut = []
for combi in workCombis:
  # if combi == ((3,2),(4,7),(6,1)):
    # print("Drinnen!")
  one, two, three = combi
  if two[0] == one[0]+1 and three[1] == two[1]-1:
    finalOut.append(combi)
  if three[1]+1 == one[1] and one[0]+1 == two[0]:
    finalOut.append(combi)    


print(finalOut)