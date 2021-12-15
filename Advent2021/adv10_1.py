with open("adv10.txt","r") as f:
  listInp = [x.strip() for x in f.readlines()]

sumPoints = 0
for elemInp in listInp:
  workElem = elemInp
  workstop = False
  while True:
    for idxChar, elemChar in enumerate(workElem):
      if elemChar in ["(","[","{","<"]:
        if idxChar == len(workElem) - 1:
          workstop = True
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

print(sumPoints)






    # if elemChar in [")","]","}",">"]:
    #   if elemChar == ")" and workElem[idxChar - 1] != "("

