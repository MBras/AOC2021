lines = open("input.1").read()
#lines = open("input.test").read()
lines = lines.splitlines()

sequence = lines.pop(0)

boards = []

for i in range(int(len(lines) / 6)):
    board = []
    lines.pop(0)
    for j in range(5):
        board.append([int(c) for c in lines.pop(0).split()])

    boards.append(board)

for s in sequence.split(","):
    # croos the number of all of the boards
    for i in range(len(boards)):
        for x in range(len(boards[i])):
            for y in range(len(boards[i][x])):
                boards[i][x][y] = "-" if boards[i][x][y] == int(s) else boards[i][x][y]

    # check for empty row or column
    for i in range(len(boards)):
        for x in range(len(boards[i])):
            if boards[i][x].count("-") == len(boards[i][x]):
                print("Done at sequence: " + str(s))
                print(boards[i])
                bs = 0
                for j in boards[i]:
                    bs += sum([z for z in j if z != "-" ])
                print(bs * int(s))
                quit()
