import os 
import sys
import string

path = os.path.abspath(os.path.dirname(sys.argv[0])) 
fn = os.path.join(path, "inp.txt")
with open(fn, encoding="utf8", errors="ignore") as f:
  lines = f.read().splitlines()

countSave = 0
for r in lines:
  workerBase = r.split()
  workerBase = [int(x) for x in workerBase]

  for idxWorkBase in range(len(workerBase)): 
    worker = workerBase[:]
    del worker[idxWorkBase]

    safeFlag = True
    if worker != sorted(worker) and worker != sorted(worker, reverse=True):
      continue
    if worker[0] > worker[1]:
      maxVal = 999999999
      for i,e in enumerate(worker):
        if e >= maxVal:
          safeFlag = False
          break
        if maxVal != 999999999 and abs(e - maxVal) > 3:
          safeFlag = False
          break        
        maxVal = e
    else:
      minVal = -1
      for i,e in enumerate(worker):
        if e <= minVal:
          safeFlag = False
          break
        if minVal != -1 and abs(e - minVal) > 3:
          safeFlag = False
          break        
        minVal = e        

    if safeFlag:
      # print(r)
      # input("Press!")
      countSave +=1
      break

print(countSave)   






















