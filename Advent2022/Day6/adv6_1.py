with open("inp.txt","r") as f:
  listInp = [x for x in f.readlines()]
workString = listInp[0]

for i,c in enumerate(workString, start=1):
  if i < 4:
    continue
  worker = workString[i-4:i]
  worker = list(worker)
  if len(list(set(worker))) == len(worker):
    print(i)
    break