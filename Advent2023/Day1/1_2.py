import os 
import sys
import string

if __name__ == '__main__':
  path = os.path.abspath(os.path.dirname(sys.argv[0])) 
  fn = os.path.join(path, "inp.txt")
  with open(fn, encoding="utf8", errors="ignore") as f:
    lines = f.read().splitlines()

  matching = [["one","1"], ["two","2"], ["three","3"], ["four","4"], ["five","5"],
              ["six","6"], ["seven","7"], ["eight","8"], ["nine","9"]]
  for i,l in enumerate(lines):
    while True:
      breakOut = False
      for iC, c in enumerate(l):
        if breakOut:
          break
        for m in matching:
          if l[iC:].startswith(m[0]):
            lines[i] = lines[i].replace(m[0], m[1])
            l = l.replace(m[0], m[1])
            breakOut = True
            break      
      
      if not breakOut:
        break
  # print(lines)
  # exit()

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