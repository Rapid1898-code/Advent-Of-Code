with open("adv1.txt","r") as f:
  listInp = [x.strip() for x in f.readlines()]

maxCal = 0
workSum = 0
for e in listInp:
  if e == "":
    if workSum > maxCal:
      maxCal = workSum
    workSum = 0
  else:
    workSum += int(e)
print(maxCal)