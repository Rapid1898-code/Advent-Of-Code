with open("adv2.txt","r") as f:
  listInp = [x.strip() for x in f.readlines()]
  listInp = [(x.split()[0].strip(), x.split()[1].strip()) for x in listInp]

countPoints = 0
for e in listInp:
  if e[1] == "X":                                     # rock: A, X
    wPoints = 1                                       # paper: B, Y
  elif e[1] == "Y":                                   # scissor: C, Z
    wPoints = 2
  elif e[1] == "Z":
    wPoints = 3
  
  # draw
  if e[0] in ["A"] and e[1] in ["X"]:
    wPoints += 3
  if e[0] in ["B"] and e[1] in ["Y"]:
    wPoints += 3
  if e[0] in ["C"] and e[1] in ["Z"]:
    wPoints += 3

  # win
  if e[0] in ["A"] and e[1] in ["Y"]:
    wPoints += 6
  if e[0] in ["B"] and e[1] in ["Z"]:
    wPoints += 6
  if e[0] in ["C"] and e[1] in ["X"]:
    wPoints += 6

  # input(wPoints)
  countPoints += wPoints

print(countPoints)










