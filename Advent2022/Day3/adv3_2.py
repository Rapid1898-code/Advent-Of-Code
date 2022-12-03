with open("adv3.txt","r") as f:
  listInp = [x.strip() for x in f.readlines()]

sumPrio = 0
for i,e in enumerate(listInp,start=1):
  if i % 3 == 0:
    wAct = list(e)
    wActMin1 = list(listInp[i-2])
    wActMin2 = list(listInp[i-3])
    for c in wAct:
      if c in wActMin1 and c in wActMin2:
        break
    if c.islower():
      wPrio = ord(c) - 96
    if c.isupper():
      wPrio = ord(c) - 38
    sumPrio += wPrio
print(sumPrio)