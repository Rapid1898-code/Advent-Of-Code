import re

#lines = ["value 5 goes to bot 2","bot 2 gives low to bot 1 and high to bot 0","value 3 goes to bot 1", "bot 1 gives low to output 1 and high to bot 0","bot 0 gives low to output 2 and high to output 0","value 2 goes to bot 2"]
with open("input10.txt") as f:
    lines = [x.strip() for x in f.readlines()]

bots = {}
output = {}
ongoing = True

while ongoing:
    for idx_l, cont in enumerate(lines):
        if 0 in output and 1 in output and 2 in output: ongoing = False
        idx = 0
        start = 0
        if cont == "": continue
        l = cont.split()
        if l[0] == "value":
            bot = int(l[5])
            val = int(l[1])
            if bot in bots:
                bot_val = bots[bot]
                bot_val[0] = val
                bot_val.sort()
                bots[bot] = bot_val
            else:
                bots[bot] = [0,val]
        elif l[0] == "bot":
            bot = int(l[1])
            if bot not in bots or bots[bot][0] == 0: continue
            #if bots[bot] == [17,61]:
            #    print ("Ergebnis Bot: ",bot)

                #bots = {k: v for k, v in sorted (bots.items (), key=lambda item: item[0], reverse=False)}
                #output = {k: v for k, v in sorted (output.items (), key=lambda item: item[0], reverse=False)}
                #print ("Working On: ", l)
                #print ("Bots: ", bots)
                # print ("Input: ",lines)
                #print ("Output: ", output)

                #ongoing = False
                #break
            if "output" not in l:
                bot2 = int(l[6])
                bot3 = int(l[11])
                if bot2 in bots:
                    bot_val = bots[bot2]
                    if bot_val[0] != 0: print ("Error1 - 2 Werte bei Zuordung!", bot2, bots[bot2])
                    bot_val[0] = bots[bot][0]
                    bot_val.sort()
                    bots[bot2] = bot_val
                else:
                    bots[bot2] = [0,bots[bot][0]]
                if bot3 in bots:
                    bot_val = bots[bot3]
                    if bot_val[0] != 0: print ("Error2 - 2 Werte bei Zuordung!", bot3, bots[bot3])
                    bot_val[0] = bots[bot][1]
                    bot_val.sort()
                    bots[bot3] = bot_val
                else:
                    bots[bot3] = [0,bots[bot][1]]
                    del bots[bot]

            elif l[5] == "output" and l[10] == "output":
                out1 = int(l[6])
                out2 = int(l[11])
                output[out1] = bots[bot][0]
                output[out2] = bots[bot][1]
                del bots[bot]
            elif l[5] == "output" and l[10] == "bot":
                out1 = int(l[6])
                bot2 = int(l[11])
                output[out1] = bots[bot][0]
                if bot2 in bots:
                    bot_val = bots[bot2]
                    bot_val[0] = bots[bot][1]
                    bot_val.sort()
                    bots[bot2] = bot_val
                else:
                    bots[bot2] = [0,bots[bot][1]]
                del bots[bot]
            else: print ("Error - Passt nicht...")
        lines[idx_l] = ""
        bots = {k: v for k, v in sorted (bots.items (), key=lambda item: item[0], reverse=False)}
        output = {k: v for k, v in sorted (output.items (), key=lambda item: item[0], reverse=False)}

        print ("Working On: ",l)
        print ("Bots: ",bots)
        #print ("Input: ",lines)
        print ("Output: ",output,"\n")
print (output[0]*output[1]*output[2])

