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
    wTest = int(inp[idx + 3].split()[-1].strip())
    wTrue = int(inp[idx + 4].split()[-1].strip())
    wFalse = int(inp[idx + 5].split()[-1].strip())
    dictMonkies[wNum] = [wItems, wOperation, wTest, wTrue, wFalse, 0]
  idx += 1
  
for i in range(20):
  for k,v in dictMonkies.items():
    for e in v[0]:
      dictMonkies[k][-1] += 1
      worker = eval(v[1].replace("old",str(e))) // 3
      if worker % v[2] == 0:
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
erg = checkVal[-1] * checkVal[-2]
print(erg)




