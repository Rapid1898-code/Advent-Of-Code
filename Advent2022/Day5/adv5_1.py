with open("inp.txt","r") as f:
  listInp = [x for x in f.readlines()]

wIDX = listInp.index("\n")
inp1 = listInp[:wIDX]
inp2 = listInp[wIDX + 1:]

dictStack = {}
for idx, r in enumerate(inp1, start=1):
  if r[1] == "1":
    break
  workLine = []
  for cIDX, cVal in enumerate(r):
    if (cIDX-1) % 4 == 0: 
      # print(cIDX, cVal)
      worker = cVal.split()
      if len(worker) > 0:
        worker = worker[0]
        workLine.append(worker)
      else: 
        workLine.append("")
  for i,e in enumerate(workLine, start=1):
    if e == "":
      continue
    if i not in dictStack:
      dictStack[i] = [e]
    else:
      dictStack[i].append(e)
dictStack = {k: v for k, v in sorted(dictStack.items(), key=lambda item: item[0])}
# for k,v in dictStack.items():
#   print(k,v)
# exit()

inpMoves = []
for r in inp2:
  worker = r.split()
  worker = [int(x) for x in worker if x.isdigit()]
  inpMoves.append(worker)
# for e in inpMoves:
#   print(e)
# exit()

def changeItems (count, lFrom, lTo):
  for i in range(count):
    lTo.insert(0,lFrom[0])
    lFrom.pop(0)
  # print(lFrom)
  # print(lTo)
  return(lFrom, lTo)

  print(count, l1, l2)
  exit()

for r in inpMoves:
  dictStack[r[1]], dictStack[r[2]]= changeItems(r[0], dictStack[r[1]], dictStack[r[2]])
  # for k,v in dictStack.items():
  #   print(k,v)
  # input("Press!")

finalString = ""
for k,v in dictStack.items():
  finalString += v[0]

print(finalString)
