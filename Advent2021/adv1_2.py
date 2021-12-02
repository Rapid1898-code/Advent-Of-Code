with open("adv1.txt","r") as f:
    listInp = [int(x.strip()) for x in f.readlines()]

countIncrease = 0
for i,e in enumerate(listInp):
  if i < 3:
    continue
  if sum(listInp[i-2:i+1]) > sum(listInp[i-3:i]):
    countIncrease += 1
print(countIncrease)