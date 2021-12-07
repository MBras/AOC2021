line = open("input.1").read()
line = open("input.test").read()

crabs = [int(i) for i in line.split(",")]

# distance cost table
dc = {} 
dc[0] = 0
for i in range(1, max(crabs) - min(crabs)):
    dc[i] = dc[i - 1] + i

print(dc)

minfuel = 9999999999999999999999999999999999999
for i in range(min(crabs), max(crabs) + 1):
    fuel = 0
    for crab in crabs:
        distance = abs(crab - i)
        cost = 0
        for j in range(1, distance + 1):
            cost += j
        fuel += cost

    if fuel < minfuel:
        minfuel = fuel
print(minfuel)
