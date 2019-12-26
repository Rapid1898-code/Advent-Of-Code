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
#liste = [['TurnOn', 0, 0, 0, 0],['Toggle', 0, 0, 999, 999]]
for action in liste:
    for x_wert in range(action[1], action[3]+1):
        for y_wert in range(action[2], action[4]+1):
            if action[0] == "TurnOn": grid[x_wert][y_wert] += 1
            elif action[0] == "TurnOff" and grid[x_wert][y_wert] > 0: grid[x_wert][y_wert] -= 1
            elif action[0] == "Toggle": grid[x_wert][y_wert] += 2

for x_achse in grid:
    for grid in x_achse:
        brightness += grid

print("Brightness: ",brightness)


