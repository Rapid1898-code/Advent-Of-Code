# import stackprinter
# stackprinter.set_excepthook(style='darkbg2')

with open("inp.txt","r") as f:
  inp = [x.strip() for x in f.readlines()]

def changePos(head, tail, wDir, wLen, posFinds):
  posH_X, posH_Y = head
  posT_X, posT_Y = tail
  # print(head, tail, wDir, wLen)

  for i in range(wLen):
    # change head position
    if wDir == "L":
      posH_X -= 1
    elif wDir == "R":
      posH_X += 1
    elif wDir == "U":
      posH_Y += 1
    elif wDir == "D":
      posH_Y -= 1

    if abs(posH_X - posT_X) > 1 and posH_Y == posT_Y:
      if posH_X > posT_X:
        posT_X = posH_X - 1
      else:
        posT_X = posH_X + 1
    elif abs(posH_X - posT_X) > 1 and posH_Y != posT_Y:
      if posH_X > posT_X:
        posT_X = posH_X - 1
      else:
        posT_X = posH_X + 1
      posT_Y = posH_Y
    elif abs(posH_Y - posT_Y) > 1 and posH_X == posT_X:
      if posH_Y > posT_Y:
        posT_Y = posH_Y - 1
      else:
        posT_Y = posH_Y + 1
    elif abs(posH_Y - posT_Y) > 1 and posH_X != posT_X:
      if posH_Y > posT_Y:
        posT_Y = posH_Y - 1
      else:
        posT_Y = posH_Y + 1
      posT_X = posH_X

    # adapt tail position
    if abs(posH_X - posT_X) > 1:
      if posH_X > posT_X:
        posT_X = posH_X - 1
<<<<<<< HEAD
      elif posH_X == 0:
        if posT_X < 0:
          posT_X = -1
        else:
          posT_X = 1
  
=======
      elif posH_X > posT_X:
       posT_X = posH_X + 1        

      # if posH_X < 0:
      #   posT_X = posH_X - 1
      # elif posH_X > 0:
      #   posT_X = posH_X + 1
      # elif posH_X == 0:
      #   if posT_X < 0:
      #     posT_X = -1
      #   else:
      #     posT_X = 1

      posT_Y = posH_Y
    
    if abs(posH_Y - posT_Y) > 1:
      if posH_Y > 0:
        posT_Y += 1
        if posH_X > posT_X:
          posT_X += 1
        if posH_X < posT_X:
          posT_X -= 1
      elif posH_Y < 0:
        posT_Y -= 1
        if posH_X > posT_X:
          posT_X += 1
        if posH_X < posT_X:
          posT_X -= 1
      elif posH_Y == 0:
        if posT_Y < 0:
          posT_Y = -1
          posT_X = 0
        else:
          posT_Y = 1
          posT_X = 0    
         
>>>>>>> 39bb380396617ed02ec6d75ed5e3914d79bbffdf
    if [posT_X, posT_Y] not in posFinds:
      posFinds.append([posT_X, posT_Y])

    if head == [1, 3] and \
       tail == [2, 4] and \
       wDir == "R" and \
       wLen == 4:
      print(f"Round: {i+1}")
      print(f"H: {posH_X, posH_Y}")
      print(f"T: {posT_X, posT_Y}")
      input("Press!")

  return([posH_X, posH_Y], [posT_X, posT_Y], posFinds)


posFinds = []
posHead = [0,0]
posTail = [0,0]
for e in inp:
  wDir = e.split()[0]
  wLen = int(e.split()[1])
  # print (posHead, posTail, e)
  posHead, posTail, posFinds = changePos(posHead, posTail, wDir, wLen, posFinds)
  # print (posHead, posTail)
  # print (posFinds)
  # input("Press!")
print(len(posFinds))

  



