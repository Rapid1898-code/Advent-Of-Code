import re

lines = ["value 5 goes to bot 2","bot 2 gives low to bot 1 and high to bot 0","value 3 goes to bot 1", "bot 1 gives low to output 1 and high to bot 0","bot 0 gives low to output 2 and high to output 0","value 2 goes to bot 2"]
#with open("input10.txt") as f:
#    lines = [x.strip() for x in f.readlines()]

bots = {}
output = {}

while True:
    for idx_l, cont in enumerate(lines):
        idx = 0
        start = 0
        if cont == "": continue
        elif cont[0] == "v":
            while idx < len(cont):
                if cont[idx].isdigit() and start == 0:
                    start = idx
                    while cont[idx].isdigit(): idx += 1
                    val = int(cont[start:idx])
                    continue
                if cont[idx].isdigit() and start != 0:
                    bot = int(cont[idx:])
                    break
                idx += 1
            if bot in bots:
                bot_val = bots[bot]
                bot_val[0] = val
                bot_val.sort()
                bots[bot] = bot_val
            else:
                bots[bot] = [0,val]

        elif cont[0] == "b":
            bot = bot2 = bot3 = 0
            if bot not in bots: continue
            if len(bots[bot]) < 2: continue
            idx = 4
            erg_bot = [m.start () for m in re.finditer ('bot', cont)]
            erg_out = [m.start () for m in re.finditer ('output', cont)]
            while cont[idx].isdigit (): idx += 1
            bot = int(cont[4:idx])
            if bots[bot] == [17,61]:
                print ("Ergebnis Bot: ",bot)
                break
            if len(erg_bot) == 3:
                idx = erg_bot[1]+4
                while cont[idx].isdigit (): idx += 1
                bot2 = int(cont[erg_bot[1]+4:idx])
                bot3 = int(cont[erg_bot[2]+4:])

                if bot2 in bots:
                    bot_val = bots[bot2]
                    bot_val[0] = bots[bot][0]
                    bot_val.sort()
                    bots[bot2] = bot_val
                else:
                    bots[bot2] = [0,bots[bot][0]]
                if bot3 in bots:
                    bot_val = bots[bot3]
                    bot_val[0] = bots[bot][1]
                    bot_val.sort()
                    bots[bot3] = bot_val
                else:
                    bots[bot3] = [0,bots[bot][1]]
                del bots[bot]

            elif len(erg_bot) == 2 and len(erg_out) == 1:
                idx = erg_out[0]+7
                while cont[idx].isdigit (): idx += 1
                out1 = int(cont[erg_out[0]+7:idx])
                bot2 = int(cont[erg_bot[1]+4:])

                output[out1] = bots[bot][0]
                if bot2 in bots:
                    bot_val = bots[bot2]
                    bot_val[0] = bots[bot][1]
                    bot_val.sort()
                    bots[bot2] = bot_val
                else:
                    bots[bot2] = [0,bots[bot][1]]
                del bots[bot]

            elif len(erg_bot) == 1 and len(erg_out) == 2:
                idx = erg_out[0]+7
                while cont[idx].isdigit (): idx += 1
                out1 = int(cont[erg_out[0]+7:idx])
                out2 = int(cont[erg_out[1]+7:])

                output[out1] = bots[bot][0]
                output[out2] = bots[bot][1]
                del bots[bot]

            else: print ("Error - Passt nicht...")
        lines[idx_l] = ""
        print (bots)
        print (lines)


