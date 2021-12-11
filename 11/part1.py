import os
import time

lines = open("input.1").read()
#lines = open("input.test").read()
cave = [[int(i) for i in list(line)] for line in lines.splitlines()]

def showcave(cave, step):
#    os.system("clear")
    print("After step " + str(step) + ":")
    for line in cave:
        print(''.join(["\033[1;37m" + str(i) + "\033[0m" if i == 0 else str(i) for i in line]))
    print("")
#    time.sleep(0.1)

def flash(cave, row, col):
    if row >= 0 and col >= 0 and row < len(cave) and col < len(cave[0]) and cave[row][col] != 0:
        cave[row][col] += 1
        if cave[row][col] > 9:
            # flashing
            cave[row][col] = 0

            for x in range(-1, 2):
                for y in range(-1, 2):
                    if not(x == 0 and y == 0):
                        cave = flash(cave, row + x, col + y)
    return cave

def countflashes(cave):
    return sum(sum(1 for i in line if i == 0) for line in cave)

def step(cave):
    for row in range(len(cave)):
        for col in range(len(cave[row])):
            cave[row][col] += 1

    for row in range(len(cave)):
        for col in range(len(cave[row])):
            if cave[row][col] > 9: 
                cave = flash(cave, row, col)
    return cave

steps = 100
score = 0

for i in range(1, steps + 1):
    cave = step(cave)
    showcave(cave, i)
    score += countflashes(cave)

print("Score: " + str(score))
