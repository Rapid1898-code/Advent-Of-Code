with open("adv3.txt","r") as f:
  listInp = [x.strip() for x in f.readlines()]

countListZero = [0 for i in range(len(listInp[0]))]
countListOne = [0 for i in range(len(listInp[0]))]

for e in listInp:
  for i,c in enumerate(e):
    if c == "0":
      countListZero[i] += 1
    else:
      countListOne[i] += 1

gamma = ""
epsilon = ""
for i,e in enumerate(countListZero):
  if e > countListOne[i]:
    gamma += "0"
    epsilon += "1"
  elif e < countListOne[i]:
    gamma += "1"
    epsilon += "0"
  else:
    print(f"Error - count of 0 and 1 is equal...")
gamma = int(gamma, 2)
epsilon = int(epsilon, 2)
erg = gamma * epsilon
print(erg)
  


