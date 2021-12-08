import re

lines = open("input.1").read()
#lines = open("input.test").read()
lines = lines.splitlines()

counter = 0

for line in lines:
    matches = re.match("(\w*) (\w*) (\w*) (\w*) (\w*) (\w*) (\w*) (\w*) (\w*) (\w*) \| (\w*) (\w*) (\w*) (\w*)", line)

    # count 1,4,7 and 8
    for i in range(11, 15):
        if len(matches.group(i)) in [2, 3, 4, 7]:
            print(matches.group(i))
            counter += 1
print(counter)
