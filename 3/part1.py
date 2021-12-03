import re
from collections import Counter

lines = open("input.1").read()
#lines = open("input.test").read()
lines = lines.splitlines()

def column(matrix, i):
    return [row[i] for row in matrix]

keys = []

gamma = ""
epsilon = ""

for line in lines:
    keys.append( list(line) )

for col in range(len(keys[0])):
    if Counter(column(keys, col))["1"] > Counter(column(keys, col))["0"]:
        gamma += "1"
        epsilon += "0"
    else:
        gamma += "0"
        epsilon += "1"

print(int(gamma,2) * int(epsilon,2))
