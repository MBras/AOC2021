from collections import Counter

line = open("input.1").read()
#line = open("input.test").read()

fish = [int(i) for i in line.split(",")]

days = 256 

fish = Counter(fish)
print(fish)

# create a list from 0 -> 8 and use this to record the number of fish for every age
for day in range(1, days + 1):
    newfish = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}
    for i in fish:
        if i == 0:
            newfish[6] += fish[i]
            newfish[8] += fish[i]
        else:
            newfish[i - 1] += fish[i]
    
    fish = newfish
    print(fish)
    print("After " + str(day) + " days: " + str(sum(fish.values())) + " fish.")
