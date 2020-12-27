# publicKeyCard = 5764801
# publicKeyDoor = 17807724

publicKeyCard = 14012298
publicKeyDoor = 74241

subjectNumber = 7
value = 1
loopSizeCard = 0
loopSizeDoor = 0
for i in range(1,1000000000):
    if i % 10000 == 0:
        print(i)
    value = value * 7
    value = value % 20201227
    # print(f"Round: {i+1} Value: {value}")
    if value == publicKeyCard:
        loopSizeCard = i
    if value == publicKeyDoor:
        loopSizeDoor = i
    if loopSizeDoor != 0 and loopSizeCard != 0:
        print(f"LoopSizeCard: {loopSizeCard}")
        print(f"LoopSizeDoor: {loopSizeDoor}")
        print("\n")
        break


print(f"PublicKeyCard: {publicKeyCard}")
print(f"LoopSizeDoor: {loopSizeDoor}")
start = 1
for i in range(loopSizeDoor):
    start = start * publicKeyCard
    start = start % 20201227
    # print (f"Round: {i + 1} Value: {start}")
print(f"EncryptKey Door: {start}")
print("\n")

print (f"PublicKeyDoor: {publicKeyDoor}")
print (f"LoopSizeCard: {loopSizeCard}")
start = 1
for i in range (loopSizeCard):
    start = start * publicKeyDoor
    start = start % 20201227
    # print (f"Round: {i + 1} Value: {start}")
print (f"EncryptKey Door: {start}")



