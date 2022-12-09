# import stackprinter
# stackprinter.set_excepthook(style='darkbg2')

with open("inp.txt","r") as f:
  inp = [x.strip() for x in f.readlines()]

workDir = []
dictPaths = {}
idx = 0
while idx < len(inp): 
  # print(idx, inp[idx])
  # print(workDir)
  # for k,v in dictPaths.items():
  #   print(k,v)
  # input("Press!")
  if "$ cd" in inp[idx]:
    if ".." in inp[idx]:
      workDir.pop()
    else:
      workDir.append(inp[idx].split()[-1])
      if tuple(workDir) not in dictPaths:
        dictPaths[tuple(workDir)] = 0
    idx += 1
  elif "ls" in inp[idx]:
    while idx+1 < len(inp) and inp[idx+1][0] != "$":
      # print(idx, inp[idx])
      # print(workDir)
      # for k,v in dictPaths.items():
      #   print(k,v)
      # input("Press!")
      idx += 1
      if "dir" in inp[idx]:
        worker = workDir[:]
        worker.append(inp[idx].split()[-1])
        if tuple(worker) not in dictPaths:
          dictPaths[tuple(worker)] = 0
      else:
        # print(inp[idx])
        wVal = int(inp[idx].split()[0])
        wList = workDir[:]
        while wList != []:
          dictPaths[tuple(wList)] += wVal
          wList.pop()
    idx += 1

valSmallest = 999999999
currentUnusedSpace = 70000000 - dictPaths[('/',)]
for k,v in dictPaths.items():
  # print(v)
  # print(valSmallest)
  # input("Press!")
  if currentUnusedSpace + v < 30000000:
    continue
  if v < valSmallest:
    valSmallest = v
print(valSmallest)
exit()




findUnused = 999999999
base = currentUnusedSpace
erg = False
for k,v in dictPaths.items():
  if base - v <= 30000000:
    continue
  w = base - v
  # print(w)
  # print(findUnused)
  # input("PresS!")
  if w < findUnused:
    findUnused = w
    erg = v
print(erg)