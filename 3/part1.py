lines = open("input.1").read()
#lines = open("input.test").read()
keys = [list(line) for line in lines.splitlines()] 

def column(matrix, i):
    return [row[i] for row in matrix]

gamma   = ""
epsilon = ""

for col in range(len(keys[0])):
    gamma   += "1" if column(keys, col).count("1") > column(keys, col).count("0") else "0"
    epsilon += "0" if gamma[-1] == "1" else "1"

print(int(gamma,2) * int(epsilon,2))
