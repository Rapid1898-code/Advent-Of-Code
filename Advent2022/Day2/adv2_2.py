with open("adv2.txt","r") as f:
  listInp = [x.strip() for x in f.readlines()]
  listInp = [(x.split()[0].strip(), x.split()[1].strip()) for x in listInp]

countPoints = 0
for e in listInp:
  if e[1] == "X":                                     # rock: A, X
    wPoints = 0                                       # paper: B, Y
    if e[0] == "A": wPoints += 3                      # scissor: C, Z
    elif e[0] == "B": wPoints += 1
    elif e[0] == "C": wPoints += 2  
  elif e[1] == "Y":                                   
    wPoints = 3
    if e[0] == "A": wPoints += 1    
    elif e[0] == "B": wPoints += 2
    elif e[0] == "C": wPoints += 3  
  elif e[1] == "Z":
    wPoints = 6
    if e[0] == "A": wPoints += 2    
    elif e[0] == "B": wPoints += 3
    elif e[0] == "C": wPoints += 1    

  # input(wPoints)
  countPoints += wPoints

print(countPoints)










