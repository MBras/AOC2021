import re

def foldup(paper, row):
    print("Folding up at row: " + str(row))
    for line in range(row - (len(paper) - row) + 1, row):
        templine = paper.pop()
        for col in range(len(paper[0])):
            if paper[line][col] == "#" or templine[col] == "#":
                paper[line][col] = "#"
    # pop the foldline
    paper.pop()
    return paper

def foldleft(paper, col):
    temppaper = [["."] * col for i in range(len(paper))]
    print("Folding left at col: " + str(col))
    for col in range(col):
        for row in range(len(paper)):
            if paper[row][col] == "#" or paper[row][-1 - col] == "#":
                temppaper[row][col] = "#"
    return temppaper

def fold(paper, instructions):
    for instruction in instructions:
        print("")
        if instruction[0] == "y":
            paper = foldup(paper, instruction[1])
        if instruction[0] == "x":
            paper = foldleft(paper, instruction[1])
        for line in paper:
            print(''.join(line))
        print(sum(line.count("#") for line in paper))

def readinput(lines):
    stars = []
    foldinstructions = []

    # first read all coordiantes until an empty line is reached
    maxx = 0
    maxy = 0
    line = lines.pop(0)
    while line != "":
        if int(line.split(",")[0]) > maxx:
            maxx = int(line.split(",")[0])
        if int(line.split(",")[1]) > maxy:
            maxy = int(line.split(",")[1])
        stars.append([int(i) for i in line.split(",")])
        line = lines.pop(0)

    # draw all the stars omn the paper
    paper = [["."] * (maxx + 1) for i in range(maxy + 1)]
    for star in stars:
        paper[star[1]][star[0]] = "#"
    for line in paper:
        print(''.join(line))

    # get all folds
    instructions = []
    for line in lines:
        matches = re.search("fold along (\D)=(\d*)", line)
        instructions.append([matches.group(1), int(matches.group(2))])

    return paper, instructions
    

lines = open("input.test").read().splitlines()
lines = open("input.1").read().splitlines()

[paper, instructions] = readinput(lines)
print(instructions)
fold(paper, instructions)
