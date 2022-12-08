# import stackprinter
# stackprinter.set_excepthook(style='darkbg2')

with open("inp.txt","r") as f:
  inp = [x.strip() for x in f.readlines()]

countVisible = len(inp) * 2
countVisible += (len(inp[0]) - 2) * 2
ergScenicScore = 0

for idxY, row in enumerate(inp):
  for idxX, c in enumerate(row):
    leftFree = rightFree = topFree = bottomFree = 1
    
    if idxY == 0 or idxX == 0 or idxY == len(inp) - 1 or idxX == len(inp[0]) - 1:
      continue    
    # print(f"Check {c} in {row}")
    # print(f"Y/X: {idxY, idxX}")

    # check left    
    checkX = idxX
    workScore = 0
    while checkX > 0:
      checkX -= 1                    
      if int(c) <= int(inp[idxY][checkX]):
        workScore += 1           
        break
      else:                      
        workScore += 1
    leftFree = workScore

    #check right
    checkX = idxX
    workScore = 0
    while checkX < len(inp[0]) - 1:      
      checkX += 1                
      if int(c) <= int(inp[idxY][checkX]):
        workScore += 1  
        break     
      else:                      
        workScore += 1
    rightFree = workScore

    #check top
    checkY = idxY
    workScore = 0
    while checkY > 0:
      checkY -= 1             
      if int(c) <= int(inp[checkY][idxX]):
        workScore += 1  
        break
      else:                      
        workScore += 1    
    topFree = workScore      

    #check bottom
    checkY = idxY
    workScore = 0
    while checkY < len(inp) - 1:
      checkY += 1                       
      if int(c) <= int(inp[checkY][idxX]):
        workScore += 1  
        break
      else:                      
        workScore += 1        
    bottomFree = workScore            
    
    workScore = leftFree * rightFree * topFree * bottomFree
    if workScore > ergScenicScore:
      ergScenicScore = workScore
    # print(leftFree, rightFree, topFree, bottomFree)
    # input("Press!")

print(ergScenicScore)