import os 
import sys
import string

path = os.path.abspath(os.path.dirname(sys.argv[0])) 
fn = os.path.join(path, "inp.txt")
with open(fn, encoding="utf8", errors="ignore") as f:
  lines = f.read().splitlines()

l1 = []
l2 = []
for r in lines:
  worker = r.split()
  worker = [int(x) for x in worker]
  l1.append(worker[0])
  l2.append(worker[1])

dictCount = {}
for e in l2:
  if e not in dictCount:
    dictCount[e] = 1
  else:
    dictCount[e] += 1

sumScore = 0
for e in l1:
  if e in dictCount:
    sumScore += e * dictCount[e]

print(sumScore)



















