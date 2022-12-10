# import stackprinter
# stackprinter.set_excepthook(style='darkbg2')

with open("inp.txt","r") as f:
  inp = [x.strip() for x in f.readlines()]

value = 1
cycle = 0
sumSignal = 0
for e in inp:
  if e == "noop":
    cycle += 1
    if cycle == 20 or (cycle - 20) % 40 == 0:
      sumSignal += cycle * value
      # print(cycle, value, sumSignal)
      # input("Press")
  else:
    wVal = int(e.split()[-1])
    cycle += 1
    if cycle == 20 or (cycle - 20) % 40 == 0:
      sumSignal += cycle * value      
      # print(cycle, value, sumSignal)
      # input("Press")
    cycle += 1
    if cycle == 20 or (cycle - 20) % 40 == 0:
      sumSignal += cycle * value      
      # print(cycle, value, sumSignal)
      # input("Press")    
    value += wVal


print(sumSignal)



