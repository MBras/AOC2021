line = open("input.1").read()
#line = open("input.test").read()

fish = [int(i) for i in line.split(",")]

days = 80 

print("Initial state: " + ",".join([str(i) for i in fish]))

for day in range(1, days + 1):
    newfish = []
    for i in range(len(fish)):
        fish[i] -= 1
        if fish[i] == -1:
            newfish.append(8)
            fish[i] = 6
    fish += newfish
    print ("After " + str(day) + " days: " + ",".join([str(i) for i in fish]))

print(len(fish))
