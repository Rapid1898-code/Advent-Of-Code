liste = []
grid = [[0 for i in range(1000)] for j in range(1000)]
count = 0
brightness = 0

def init():
    file = open("Advent06.txt", "r")    # Input-Elemente aus Datei in Liste lesen
    for line in file:
        temp_line = line.rstrip()
        temp_action = ""
        temp_xfrom = temp_yfrom = temp_xto = temp_yto = 0
        if temp_line[0:7] == 'turn on':
            temp_action = "TurnOn"
            temp_line = temp_line[8:]
        if temp_line[0:8] == 'turn off':
            temp_action = "TurnOff"
            temp_line = temp_line[9:]
        if temp_line[0:6] == 'toggle':
            temp_action = "Toggle"
            temp_line = temp_line[7:]

        for idx, char in enumerate(temp_line):
            if temp_line[idx] == ',':
                xfrom = int(temp_line[:idx])
                temp_line = temp_line[idx+1:]
                break

        for idx, char in enumerate(temp_line):
            if temp_line[idx] == ' ':
                yfrom = int(temp_line[:idx])
            if temp_line[idx] == 'g':
                temp_line = temp_line[idx+3:]
                break

        for idx, char in enumerate(temp_line):
            if temp_line[idx] == ',':
                xto = int(temp_line[:idx])
                yto = int(temp_line[idx+1:])
                break

        liste.append([temp_action,xfrom,yfrom,xto,yto])
    file.close()

init()
liste = [['TurnOn', 0, 0, 0, 0],['Toggle', 0, 0, 999, 999]]
for action in liste:
    for x_wert in range(action[1], action[3]+1):
        for y_wert in range(action[2], action[4]+1):
            if action[0] == "TurnOn": grid[x_wert][y_wert] = 1
            elif action[0] == "TurnOff": grid[x_wert][y_wert] = 0
            elif action[0] == "Toggle":
                if grid[x_wert][y_wert] == 0: grid[x_wert][y_wert] = 1
                elif grid[x_wert][y_wert] == 1: grid[x_wert][y_wert] = 0
                else: print("Error Grid!")
            else: print("Error Actions!")
    temp_bright = (action[3]+1-action[1]) * (action[4]+1-action[2])
    if action[0] == "TurnOn":
        brightness += temp_bright
    elif action[0] == "TurnOff":
        brightness -= temp_bright
        if brightness < 0: brightness = 0
    elif action[0] == "Toggle":
        temp_bright = temp_bright * 2
        brightness += temp_bright
    else: print ("Error Brightness!")

for x_achse in grid:
    for grid in x_achse:
        if grid == 1: count += 1

print("Ligths: ",count)
print("Brightness: ",brightness)


