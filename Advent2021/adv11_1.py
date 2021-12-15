with open("adv11.txt","r") as f:
  listInp = [list(x.strip()) for x in f.readlines()]
for i,e in enumerate(listInp):
  listInp[i] = [int(x) for x in listInp[i]]

workInp = listInp[:]
countFlashes = 0
for i in range(100):
  for X in range(len(workInp[0])):
    for Y in range(len(workInp)):
      workInp[Y][X] += 1
  while True:
    checkInp = workInp[:]
    for X in range(len(workInp[0])):
      for Y in range(len(workInp)):
        if workInp[Y][X] >= 10:
          workInp[Y][X] = 0
          if X-1 >= 0 and workInp[Y][X-1] != 0:
            workInp[Y][X-1] += 1
          if X-1 >= 0 and Y-1 >= 0 and workInp[Y-1][X-1] != 0:
            workInp[Y-1][X-1] += 1
          if X-1 >= 0 and Y+1 <= len(workInp)-1 and workInp[Y+1][X-1] != 0:
            workInp[Y+1][X-1] += 1
          if X+1 <= len(workInp)-1 and workInp[Y][X+1] != 0:
            workInp[Y][X+1] += 1
          if X+1 <= len(workInp)-1 and Y-1 >= 0 and workInp[Y-1][X+1] != 0:
            workInp[Y-1][X+1] += 1
          if X+1 <= len(workInp)-1 and Y+1 <= len(workInp)-1 and workInp[Y+1][X+1] != 0:
            workInp[Y+1][X+1] += 1
          if Y-1 >= 0 and workInp[Y-1][X] != 0:
            workInp[Y-1][X] += 1
          if Y+1 <= len(workInp)-1 and workInp[Y+1][X] != 0:
            workInp[Y+1][X] += 1
    if checkInp == workInp:
      break

  for X in range(len(workInp[0])):
    for Y in range(len(workInp)):
      if workInp[Y][X] >= 10:
        workInp[Y][X] = 0
        countFlashes += 1

  print(i+1)
  print(f"Count Flashes: {countFlashes}")
  for e in workInp:
    print(e)
  input()


  
