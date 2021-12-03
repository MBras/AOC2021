lines = open("input.1").read()
#lines = open("input.test").read()
keys = [list(line) for line in lines.splitlines()]

def column(matrix, i):
    return [row[i] for row in matrix]

oxygen = keys
for col in range(len(keys[0])):
    val = "1" if column(oxygen, col).count("1") >= column(oxygen, col).count("0") else "0"
    oxygen = [row for row in oxygen if row[col] == val]
    if len(oxygen) == 1:
        break

co2 = keys
for col in range(len(keys[0])):
    val = "0" if column(co2, col).count("1") >= column(co2, col).count("0") else "1"
    co2 = [row for row in co2 if row[col] == val]
    if len(co2) == 1:
        break

print(int(''.join(oxygen[0]), 2) * int(''.join(co2[0]), 2))
