import re

lines = open("input.1").read()
#lines = open("input.test").read()
lines = lines.splitlines()

# fill matrix based on lines
oceanfloor = [ [0] * 1000 for i in range(1000) ] 

for line in lines:
    coords = re.match("(\d*),(\d*) -> (\d*),(\d*)", line)
    y1 = min(int(coords[1]), int(coords[3]))
    y2 = max(int(coords[1]), int(coords[3]))
    x1 = min(int(coords[2]), int(coords[4]))
    x2 = max(int(coords[2]), int(coords[4]))

    # if x matches, fill a vertical line
    if x1 == x2:
        for y in range(y1, y2 + 1):
            oceanfloor[x1][y] += 1
    elif y1 == y2:
        for x in range(x1, x2 + 1):
            oceanfloor[x][y1] += 1
    else:
        print(line)
        xstep = 1 if int(coords[2]) < int(coords[4]) else -1
        ystep = 1 if int(coords[1]) < int(coords[3]) else -1
        steps = abs(int(coords[2]) -  int(coords[4]))
        x = int(coords[2])
        y = int(coords[1])
        for i in range(steps + 1):
            oceanfloor[x][y] += 1
            x += xstep
            y += ystep

score = 0
for line in oceanfloor:
    print("".join([str(i) for i in line]))
    score += sum(1 for i in line if i > 1)

print(score)
