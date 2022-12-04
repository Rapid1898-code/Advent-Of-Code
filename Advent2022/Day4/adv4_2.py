with open("inp.txt","r") as f:
  listInp = [x.strip() for x in f.readlines()]

countOverlaps = 0
for e in listInp:
  worker = e.split(",")
  from1 = int(worker[0].split("-")[0])
  to1 = int(worker[0].split("-")[1])
  from2 = int(worker[1].split("-")[0])
  to2 = int(worker[1].split("-")[1])
  if from1 >= from2 and from1 <= to2:
    countOverlaps += 1
  elif to1 >= from2 and to1 <= to2:
    countOverlaps += 1
  elif from2 >= from1 and from2 <= to1:
    countOverlaps += 1      
  elif to2 >= from1 and to2 <= to1:
    countOverlaps += 1
print(countOverlaps)