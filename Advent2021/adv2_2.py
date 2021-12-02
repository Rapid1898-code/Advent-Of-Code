with open("adv2.txt","r") as f:
  listInp = [x.strip() for x in f.readlines()]
  listInp = [(x.split(" ")[0], int(x.split(" ")[1])) for x in listInp]
  
  horizontPos = depthPos = aimPos = 0
  for dir, val in listInp:
    if dir == "forward":
      horizontPos += val
      depthPos += aimPos * val
    elif dir == "down":
      aimPos += val
    elif dir == "up":
      aimPos -= val      
  result = horizontPos * depthPos
  print(result)