with open("adv6.txt","r") as f:
  listInp = [x.strip() for x in f.readlines()]
listInp = listInp[0].split(',')
listInp = [int(x) for x in listInp]

for i in range(256):
  print(f"Working on round {i}...") 
  # print(listInp)
  countAdding = 0
  for idxElem, elem in enumerate(listInp):
    if elem == 0:
      listInp[idxElem] = 6
      countAdding += 1
    else:
      listInp[idxElem] -= 1
  for i in range(countAdding):
    listInp.append(8)

print(len(listInp))

    
