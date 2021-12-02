with open("adv1.txt","r") as f:
    listInp = [int(x.strip()) for x in f.readlines()]

countIncrease = 0
for i,e in enumerate(listInp):
  if i == 0:
    continue
  if e > listInp[i - 1]:
    countIncrease += 1
print(countIncrease)