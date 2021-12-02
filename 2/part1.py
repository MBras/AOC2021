import re

lines = open("input.1").read()
lines = open("input.test").read()
lines = lines.splitlines()

pos = 0
depth = 0

for line in lines:
    cmd = line.split()
    if cmd[0] == "forward":
        print("going forward")
        pos += int(cmd[1])
    elif cmd[0] == "down":
        print("going down")
        depth += int(cmd[1])
    elif cmd[0] == "up":
        print("going up")
        depth -= int(cmd[1])
    else:
        print("ERROR")
print (pos * depth)

