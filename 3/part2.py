import re
from collections import Counter

lines = open("input.1").read()
#lines = open("input.test").read()
lines = lines.splitlines()

def column(matrix, i):
    return [row[i] for row in matrix]

keys = []

for line in lines:
    keys.append( list(line) )

oxygen = keys

for col in range(len(keys[0])):
    if Counter(column(oxygen, col))["1"] >= Counter(column(oxygen, col))["0"]:
        # removde all keys with 0  at position col
        oxygen = [row for row in oxygen if row[col] == "1"]
    else:
        oxygen = [row for row in oxygen if row[col] == "0"]
    if len(oxygen) == 1:
        break

co2 = keys
for col in range(len(keys[0])):
    if Counter(column(co2, col))["1"] >= Counter(column(co2, col))["0"]:
        co2 = [row for row in co2 if row[col] == "0"]
    else:
        co2 = [row for row in co2 if row[col] == "1"]
    if len(co2) == 1:
        break

print(int(''.join(oxygen[0]), 2))
print(int(''.join(co2[0]), 2))

print(int(''.join(oxygen[0]), 2) * int(''.join(co2[0]), 2))
