with open("adv3.txt","r") as f:
  listInp = [x.strip() for x in f.readlines()]

sumPrio = 0
for e in listInp:
  worker = list(e)
  wLen = len(worker) // 2
  wPart1 = worker[:wLen]
  wPart2 = worker[wLen:]
  for c in wPart1:
    if c in wPart2:
      break
  if c.islower():
    wPrio = ord(c) - 96
  if c.isupper():
    wPrio = ord(c) - 38
  sumPrio += wPrio
print(sumPrio)