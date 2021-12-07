line = open("input.1").read()
#line = open("input.test").read()

crabs = [int(i) for i in line.split(",")]

minfuel = len(crabs) * max(crabs)
for i in range(min(crabs), max(crabs) + 1):
    fuel = 0
    for crab in crabs:
        fuel += abs(crab - i)

    if fuel < minfuel:
        minfuel = fuel
print(minfuel)
