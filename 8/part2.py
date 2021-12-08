import re

lines = open("input.1").read()
#lines = open("input.test").read()
lines = lines.splitlines()

def map_digits(data, calc):
    digits = {}
    
    # find the one
    one = [i for i in data if len(i) == 2][0]
    digits[''.join(sorted(one))] = 1
    data.remove(one)

    # find the four
    four = [i for i in data if len(i) == 4][0]
    digits[''.join(sorted(four))] = 4
    data.remove(four)

    # find the seven
    seven = [i for i in data if len(i) == 3][0]
    digits[''.join(sorted(seven))] = 7
    data.remove(seven)

    # find the eight
    eight = [i for i in data if len(i) == 7][0]
    digits[''.join(sorted(eight))] = 8
    data.remove(eight)

    # find the three (difference with the 7 is 2 wires)
    three = [i for i in data if len(i) == 5 and len(set(list(i)) - set(list(seven))) == 2][0]
    digits[''.join(sorted(three))] = 3
    data.remove(three)

    # find the six (difference with the 7 is 4 wires)
    six = [i for i in data if len(i) == 6  and len(set(list(i)) - set(list(seven))) == 4][0]
    digits[''.join(sorted(six))] = 6
    data.remove(six)

    # find the 0 (difference with the 3 is 2 wires)
    zero = [i for i in data if len(i) == 6 and len(set(list(i)) - set(list(three))) == 2][0]
    digits[''.join(sorted(zero))] = 0
    data.remove(zero)

    # find the 9, only remaining with 6 wires
    nine = [i for i in data if len(i) == 6][0]
    digits[''.join(sorted(nine))] = 9
    data.remove(nine)

    # find the 5 (difference with the four is 2 wires)
    five = [i for i in data if len(set(list(i)) - set(list(four))) == 2][0]
    digits[''.join(sorted(five))] = 5
    data.remove(five)

    # 2 is last remaining
    digits[''.join(sorted(data[0]))] = 2

    value = 0
    for i in calc:
        value = value * 10 + digits[''.join(sorted(i))]
    return value    


sum = 0
for line in lines:
    matches = re.findall("(\w*) (\w*) (\w*) (\w*) (\w*) (\w*) (\w*) (\w*) (\w*) (\w*) \| (\w*) (\w*) (\w*) (\w*)", line)
    sum += map_digits(list(matches[0][0:10]), list(matches[0][10:14]))

print(sum)
