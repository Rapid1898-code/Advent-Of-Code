with open("adv1.txt","r") as f:
  listInp = [x.strip() for x in f.readlines()]

maxCalList = [0,0,0]
workSum = 0
for e in listInp:
  if e == "":
    if workSum > min(maxCalList):
      maxCalList.remove(min(maxCalList))
      maxCalList.append(workSum)   
    workSum = 0
  else:
    workSum += int(e)
print(sum(maxCalList))