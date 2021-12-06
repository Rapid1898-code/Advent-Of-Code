with open("adv6.txt","r") as f:
  listInp = [x.strip() for x in f.readlines()]
listInp = listInp[0].split(',')
listInp = [int(x) for x in listInp]
listFinalInp = []
for i in range(9):
  countExist = 0
  for e in listInp:
    if e == i:
      countExist += 1
  listFinalInp.append(countExist)


for i in range(256):
  print(f"Working on round {i}...") 
  tmpChange = listFinalInp[0]
  listFinalInp = listFinalInp[1:]    
  listFinalInp.append(tmpChange)
  listFinalInp[6] += tmpChange
  
  print(listFinalInp)
  # input()

print(sum(listFinalInp))

    
