def check_pw(zahl):
    doppel = False
    zahl_str = str(zahl)
    for i in range(0, len(zahl_str)-1):
      if zahl_str[i]>zahl_str[i+1]:
        return False
      if zahl_str[i]==zahl_str[i+1]:
        doppel = True
    if doppel == True:
      return True
    else:
      return False

start = 152085
ende = 670283
anz_erg = 0
while start <= ende:
    if check_pw(start):
        anz_erg +=1
    start +=1

print (anz_erg)








