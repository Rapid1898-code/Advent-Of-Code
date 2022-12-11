# import stackprinter
# stackprinter.set_excepthook(style='darkbg2')

with open("inp.txt","r") as f:
  inp = [x.strip() for x in f.readlines()]

value = 1
cycle = 0
sumSignal = 0
pos = 0
for e in inp:
  print(e)
  if e == "noop":    
    print(f"Pos: {pos}, Value-1: {value-1}, Cycle: {cycle}")    
    if value - 1 == pos:
      print("#")
    else:
      print(".")
    input("Press")          
    cycle += 1
    pos += 1
    if cycle == 20 or (cycle - 20) % 40 == 0:
      sumSignal += cycle * value

      # print(cycle, value, sumSignal)
      # input("Press")
  else:
    wVal = int(e.split()[-1])
    cycle += 1
    print(f"Pos: {pos}, Value-1: {value-1}, Cycle: {cycle}")    
    if value - 1 == pos:
      print("#")
    else:
      print(".")    
    input("Press")          
    pos += 1        
    if cycle == 20 or (cycle - 20) % 40 == 0:
      sumSignal += cycle * value      
      if value - 1 == pos:
        print("#")
      else:
        print(".")      
      # print(cycle, value, sumSignal)
      # input("Press")
    cycle += 1
    value += wVal    
    print(f"Pos: {pos}, Value-1: {value-1}, Cycle: {cycle}")       
    if value - 1 == pos:
      print("#")
    else:
      print(".")      
    input("Press")            
    pos += 1        
    if cycle == 20 or (cycle - 20) % 40 == 0:
      sumSignal += cycle * value       
      # print(cycle, value, sumSignal)
      # input("Press")    
    

print(sumSignal)



