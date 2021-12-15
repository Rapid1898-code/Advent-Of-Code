with open("adv10.txt","r") as f:
  listInp = [x.strip() for x in f.readlines()]

sumPoints = 0
listInp2 = []
for elemInp in listInp:
  workElem = elemInp
  workstop = False
  while True:
    for idxChar, elemChar in enumerate(workElem):
      if elemChar in ["(","[","{","<"]:
        if idxChar == len(workElem) - 1:
          workstop = True
          listInp2.append(workElem)
          break
        else:
          continue
      elif (elemChar == ")" and workElem[idxChar - 1] == "(") \
        or (elemChar == "]" and workElem[idxChar - 1] == "[") \
        or (elemChar == "}" and workElem[idxChar - 1] == "{") \
        or (elemChar == ">" and workElem[idxChar - 1] == "<"):
          workElem = workElem[:idxChar-1] + workElem[idxChar+1:]
          break
      else:
        if elemChar == ")":
          sumPoints += 3
        elif elemChar == "]":
          sumPoints += 57
        elif elemChar == "}":
          sumPoints += 1197
        elif elemChar == ">":
          sumPoints += 25137
        workstop = True
        break
    if workstop:
      break

# reverse all strings
listInp2 = [x[::-1] for x in listInp2]
listNum = []
for elem in listInp2:
  sumPoints2 = 0
  for i,c in enumerate(elem):
    sumPoints2 *= 5
    if c == "(":
      sumPoints2 += 1
    elif c == "[":
      sumPoints2 += 2
    elif c == "{":
      sumPoints2 += 3
    elif c == "<":
      sumPoints2 += 4
  listNum.append(sumPoints2)

print(listNum)

for e in listNum:
  countLower = countUpper = 0
  for e2 in listNum:
    if e2 == e:
      continue
    if e > e2:
      countUpper += 1
    if e < e2:
      countLower += 1
  if countLower == countUpper:
    print(e)
    break


