import statistics

with open("adv8.txt","r") as f:
  listInp = [x.strip() for x in f.readlines()]
listInp = [x.split(" | ")[1].split() for x in listInp]

countErg = 0
for row in listInp:
  for elem in row:
    if len(elem) in [2,4,3,7]:
      countErg += 1
print(countErg)

