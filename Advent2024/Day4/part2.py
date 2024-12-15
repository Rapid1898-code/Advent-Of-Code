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

  leftToRight_Flag = rightToleft_Flag = False
  if (lines[y-1][x-1] == "M" and lines[y+1][x+1] == "S") or (lines[y-1][x-1] == "S" and lines[y+1][x+1] == "M"):
    leftToRight_Flag = True
  if (lines[y+1][x-1] == "M" and lines[y-1][x+1] == "S") or (lines[y+1][x-1] == "S" and lines[y-1][x+1] == "M"):
    rightToleft_Flag = True
  if leftToRight_Flag and rightToleft_Flag:
    countXMAS += 1

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
    if x == 0 or y == 0 or x == len(lines[y])-1 or y == len(lines)-1:
      continue
    if e == "A":
      erg = checkXMAS(y,x)
      ergCount += erg

print(ergCount)