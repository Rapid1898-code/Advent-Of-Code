# import stackprinter
# stackprinter.set_excepthook(style='darkbg2')
import os
import sys

path = os.path.abspath(os.path.dirname(sys.argv[0])) 
fn = os.path.join(path, "inp.txt")


dictMonkies = {}
with open(fn,"r") as f:
  inp = [x.strip() for x in f.readlines()]

idx = 0
while idx < (len(inp)):
  if "Monkey" in inp[idx]:
    wNum = int(inp[idx].split()[-1].replace(":",""))
    wItems = inp[idx + 1].split(":")[-1].strip()
    wItems = wItems.split(",")
    wItems = [int(x.strip()) for x in wItems]
    wOperation = inp[idx + 2].split("new =")[-1].strip()
    wOperation = wOperation.split()
    wOperation = [int(x) if x.isdigit() else x for x in wOperation]   
    wTest = int(inp[idx + 3].split()[-1].strip())
    wTrue = int(inp[idx + 4].split()[-1].strip())
    wFalse = int(inp[idx + 5].split()[-1].strip())
    dictMonkies[wNum] = [wItems, wOperation, wTest, wTrue, wFalse, 0]
  idx += 1
  
for i in range(1,10001):
  print(f"Round {i}")
  for k,v in dictMonkies.items():
    for e in v[0]:
      dictMonkies[k][-1] += 1
      
      if v[1][1] == "*":
        if v[1][0] == "old" and v[1][2] == "old":
          worker = (e * e)
        else:
          worker = (e * v[1][2])          
      if v[1][1] == "+":
        worker = (e + v[1][2])
      
      if int(str(worker)[-1]) in [0,2,4,6,8,5]:
        dictMonkies[v[4]][0].append(worker)
      elif worker % v[2] == 0:
        dictMonkies[v[3]][0].append(worker)
      else:
        dictMonkies[v[4]][0].append(worker)
    dictMonkies[k][0] = []
    
# for kT,vT in dictMonkies.items():
#   print(kT, vT)
# input("Press!")

checkVal = []
for k,v in dictMonkies.items():
  checkVal.append(v[-1])
checkVal.sort()
print(checkVal)
erg = checkVal[-1] * checkVal[-2]
print(erg)
