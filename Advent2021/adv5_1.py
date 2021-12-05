with open("adv5.txt","r") as f:
  listInp = [x.strip() for x in f.readlines()]
listInpFin = []
for l in listInp:
  tmpVal = l.split(" -> ")
  listInpFin.append(((int(tmpVal[0].split(",")[0]), int(tmpVal[0].split(",")[1])), \
                    (int(tmpVal[1].split(",")[0]), int(tmpVal[1].split(",")[1]))))

matchCoord = {}
for e in listInpFin:
  # check if x is equal or y is equal
  if e[0][0] != e[1][0] and e[0][1] != e[1][1]:
    continue

  if e[0][0] == e[1][0]:
    iterCoord = [e[0][1], e[1][1]]
    iterCoord.sort()
    for idx in range(iterCoord[0], iterCoord[1] + 1):
      if (e[0][0], idx) not in matchCoord:
        matchCoord[(e[0][0], idx)] = 1
      else:
        matchCoord[(e[0][0], idx)] += 1
    
  if e[0][1] == e[1][1]:
    iterCoord = [e[0][0], e[1][0]]
    iterCoord.sort()
    for idx in range(iterCoord[0], iterCoord[1] + 1):
      if (idx, e[0][1]) not in matchCoord:
        matchCoord[(idx, e[0][1])] = 1
      else:
        matchCoord[(idx, e[0][1])] += 1

countOverlaps = 0
for k,v in matchCoord.items():
  if v >= 2:
    countOverlaps += 1

print(countOverlaps)