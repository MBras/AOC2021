line = open("input.1").read()
#line = open("input.test").read()

crabs = [int(i) for i in line.split(",")]

# distance cost table
dc = {} 
dc[0] = 0
for i in range(1, max(crabs) - min(crabs) + 1):
    dc[i] = dc[i - 1] + i

minfuel = 9999999999999999999999999999999999999
for i in range(min(crabs), max(crabs) + 1):
    fuel = 0
    for crab in crabs:
        fuel += dc[abs(crab - i)]

    if fuel < minfuel:
        minfuel = fuel
print(minfuel)
