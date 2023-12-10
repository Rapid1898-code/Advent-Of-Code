import os 
import sys
import string

if __name__ == '__main__':
  path = os.path.abspath(os.path.dirname(sys.argv[0])) 
  fn = os.path.join(path, "inp.txt")
  with open(fn, encoding="utf8", errors="ignore") as f:
    lines = f.read().splitlines()

  total = 0
  for l in lines:
    firstNumber = lastNumber = False
    for c in l:
      if c in string.digits:
        if not firstNumber:
          firstNumber = c
        else:
          lastNumber = c
    if lastNumber:    
      checkNum = int(f"{firstNumber}{lastNumber}")
    else:
      checkNum = int(f"{firstNumber}{firstNumber}")
    total += checkNum
  
  print(total)