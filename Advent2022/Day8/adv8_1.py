# import stackprinter
# stackprinter.set_excepthook(style='darkbg2')

with open("inp.txt","r") as f:
  inp = [x.strip() for x in f.readlines()]

countVisible = len(inp) * 2
countVisible += (len(inp[0]) - 2) * 2

for idxY, row in enumerate(inp):
  for idxX, c in enumerate(row):
    leftFree = rightFree = topFree = bottomFree = True
    if idxY == 0 or idxX == 0 or idxY == len(inp) - 1 or idxX == len(inp[0]) - 1:
      continue    
    # print(f"Check {c} in {row}")
    # print(f"Y/X: {idxY, idxX}")

    # check left    
    checkX = idxX
    while checkX > 0:
      checkX -= 1      
      if int(c) <= int(inp[idxY][checkX]):
        leftFree = False
        break

    #check right
    checkX = idxX
    while checkX < len(inp[0]) - 1:      
      checkX += 1      
      if int(c) <= int(inp[idxY][checkX]):
        rightFree = False
        break

    #check top
    checkY = idxY
    while checkY > 0:
      checkY -= 1      
      if int(c) <= int(inp[checkY][idxX]):
        topFree = False
        break

    #check bottom
    checkY = idxY
    while checkY < len(inp) - 1:
      checkY += 1      
      if int(c) <= int(inp[checkY][idxX]):
        bottomFree = False
        break
    if leftFree or rightFree or topFree or bottomFree:
      # print("Free Sight!")
      # print(leftFree, rightFree, topFree, bottomFree)
      countVisible += 1
    # else:
    #   print("NO Free Sight!")
    # input("Press!")


print(countVisible)