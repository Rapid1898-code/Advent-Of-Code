with open("inp.txt","r") as f:
  listInp = [x for x in f.readlines()]
workString = listInp[0]

markerNum = 14
for i,c in enumerate(workString, start=1):
  if i < markerNum:
    continue
  worker = workString[i-markerNum:i]
  worker = list(worker)
  if len(list(set(worker))) == len(worker):
    print(i)
    break