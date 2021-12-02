import re

lines = open("input.1").read()
lines = lines.splitlines()

previous = lines.pop(0)
increase = 0

for current in lines:
    if current > previous :
        print(current + " (increased)")
        increase += 1
    else :
        print(current + " (decreased)")
    previous = current

print(str(increase) + " increases")
