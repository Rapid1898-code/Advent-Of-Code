import os 
import sys
import string

path = os.path.abspath(os.path.dirname(sys.argv[0])) 
fn = os.path.join(path, "inp.txt")
with open(fn, encoding="utf8", errors="ignore") as f:
  lines = f.read().splitlines()

def checkXMAS(y,x):
  listCheck = []
  countXMAS = 0
  if x >= 3 and lines[y][x-3:x+1] == "SAMX":    # check left
    countXMAS += 1
    listCheck.append("L")
  if x < len(lines[y]) - 3 and lines[y][x:x+4] == "XMAS":    # check right
    countXMAS += 1
    listCheck.append("R")    
  if y >= 3 and lines[y-1][x] == "M" and lines[y-2][x] == "A" and lines[y-3][x] == "S": # check top
    countXMAS += 1
    listCheck.append("T")    
  if y < len(lines) - 3 and lines[y+1][x] == "M" and lines[y+2][x] == "A" and lines[y+3][x] == "S": # check bottom
    countXMAS += 1
    listCheck.append("B")    

  try:  # check upper left corner
    if x >= 3 and y >= 3 and lines[y-1][x-1] == "M" and lines[y-2][x-2] == "A" and lines[y-3][x-3] == "S":
      countXMAS += 1
      listCheck.append("ULC")
  except:
    pass
  try:  # check upper right corner
    if x < len(lines[y]) - 3 and y >= 3 and lines[y-1][x+1] == "M" and lines[y-2][x+2] == "A" and lines[y-3][x+3] == "S":
      countXMAS += 1
      listCheck.append("URC")
  except:
    pass
  try:  # check lower left corner
    if x >= 3 and y < len(lines) - 3 and lines[y+1][x-1] == "M" and lines[y+2][x-2] == "A" and lines[y+3][x-3] == "S":
      countXMAS += 1
      listCheck.append("LLC")     
  except:
    pass
  try:  # check lower right corner
    if x < len(lines[y]) - 3 and x < len(lines[y]) - 3 and lines[y+1][x+1] == "M" and lines[y+2][x+2] == "A" and lines[y+3][x+3] == "S":
      countXMAS += 1
      listCheck.append("LRC")     
  except:
    pass

  # if y == 9 and x == 1:
  #   print(y,x)
  #   print(lines[y-1][x-1])
  #   print(lines[y-1][x-2])
  #   print(lines[y-1][x-3])
  #   print(countXMAS)
  #   print(listCheck)
  #   input("Press!")

  return countXMAS

ergCount = 0
for y,l in enumerate(lines):
  for x,e in enumerate(l):
    if e == "X":
      erg = checkXMAS(y,x)
      ergCount += erg

print(ergCount)