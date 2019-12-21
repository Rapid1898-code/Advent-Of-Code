import sys
from intcode import Intcode

ram = Intcode.load_prgm("Advent10.csv")
cpu = Intcode(ram)

pos = (0, 0)
dir = (0, -1)
tiles = {}
paint = True


def handle_output(output):
	global pos
	global dir
	global tiles
	global paint

	if paint:
		# paint (output = color)
		tiles[pos] = output
	else:
		if output == 0:
			# turn left
			x, y = dir
			dir = (y, -x)
		elif output == 1:
			# turn right
			x, y = dir
			dir = (-y, x)

		# move
		pos = tuple(map(sum, zip(pos, dir)))
		cpu.input(get_input())

	paint = not paint

tiles[pos] = 1 # set first tile to white
cpu.add_output(handle_output)
cpu.input(get_input())
cpu.run()

minx = min(tiles, key = lambda tile: tile[0])[0]
maxx = max(tiles, key = lambda tile: tile[0])[0]
xlen = maxx - minx + 1

miny = min(tiles, key = lambda tile: tile[1])[1]
maxy = max(tiles, key = lambda tile: tile[1])[1]
ylen = maxy - miny + 1

for y in range(ylen):
	for x in range(xlen):
		if (x - minx, y - miny) in tiles:
			sys.stdout.write('#' if tiles[(x - minx, y - miny)] == 1 else ' ')
		else:
			sys.stdout.write(' ')
	print()