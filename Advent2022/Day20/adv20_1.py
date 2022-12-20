# import stackprinter
# stackprinter.set_excepthook(style='darkbg2')
import os
import sys

path = os.path.abspath(os.path.dirname(sys.argv[0])) 
fn = os.path.join(path, "inp.txt")
with open(fn,"r") as f:
  inp = [int(x.strip()) for x in f.readlines()]

initList = inp[:]
for e in initList:
  inp.pop(0)
  inp.insert(e,e)
  print(inp)
  input()


