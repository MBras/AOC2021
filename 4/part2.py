lines = open("input.1").read()
#lines = open("input.test").read()
#lines = open("input.test2").read()
lines = lines.splitlines()

sequence = lines.pop(0)

boards = []

def crossnumber(number, board):
    return [["-" if cell == number else cell for cell in row] for row in board]

def checkbingo(board):
    # check horitzontal lines
    if [row.count("-") == len(row) for row in board].count(True) == 1:
        return True
    
    # check vertical lines
    for x in range(len(board[0])):
        rboard = [row[x] for row in board]
        if [row[x] for row in board].count("-") == len([row[x] for row in board]):
            return True

    return False

def calcscore(board):
    score = 0
    for row in board:
        score += sum([int(cell) for cell in row if cell != "-"])
    return score

for i in range(int(len(lines) / 6)):
    board = []
    lines.pop(0)
    for j in range(5):
        board.append(lines.pop(0).split())

    boards.append(board)

for s in sequence.split(","):
    newboards = []
    # croos the number of all of the boards
    for i in range(len(boards)):
        boards[i] = crossnumber(s, boards[i])
        if checkbingo(boards[i]):
            print("BINGO! for number " + s)

            # check if this is the last board to win
            if len(boards) == 1:
                print(calcscore(boards[i]) * int(s))    
        else:
            newboards.append(boards[i])
    boards = newboards
