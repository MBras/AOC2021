lines = open("input.1").read()
#lines = open("input.test").read()
lines = [[int(i) for i in list(line)] for line in lines.splitlines()]

print(lines)

def getheight(heightmap, x, y):
    try:
        return heightmap[y][x]
    except:
        return 999

risk = 0

for y in range(len(lines)):
    for x in range(len(lines[0])):
        if getheight(lines, x - 1, y) > lines[y][x] and \
           getheight(lines, x + 1, y) > lines[y][x] and \
           getheight(lines, x, y - 1) > lines[y][x] and \
           getheight(lines, x, y + 1) > lines[y][x]:
            print("Low point at: (" + str(x) + "," + str(y) + "): " + str(lines[y][x]))
            risk += (lines[y][x] + 1)

print(risk)
