heightmap = open("input.1").read()
#heightmap = open("input.test").read()
heightmap = [[int(i) for i in list(line)] for line in heightmap.splitlines()]

def getheight(inputmap, x, y):
    if x >= 0 and x < len(inputmap[0]) and y >= 0 and y < len(inputmap):
        return inputmap[y][x]
    else:
        return 9 # this is the maximum value and will stop the flow, just like a regular 9

def getfill(inputmap, x, y):
    return inputmap[y][x]

def fill(inputmap, outputmap, x, y):
    # recursive function that from (x,y) will fill all directions until a 9 
    # is reached or the area is already filled 
    # (edges will be detected based on the default return value of 9)
    outputmap[y][x] = 1
    if getheight(inputmap, x - 1, y) != 9 and getfill(outputmap, x - 1, y) != 1:
        outputmap = fill(inputmap, outputmap, x - 1, y)
    if getheight(inputmap, x + 1, y) != 9 and getfill(outputmap, x + 1, y) != 1:
        outputmap = fill(inputmap, outputmap, x + 1, y)
    if getheight(inputmap, x, y - 1) != 9 and getfill(outputmap, x, y - 1) != 1:
        outputmap = fill(inputmap, outputmap, x, y - 1)
    if getheight(inputmap, x, y + 1) != 9 and getfill(outputmap, x, y + 1) != 1:
        outputmap = fill(inputmap, outputmap, x, y + 1)

    return outputmap

def printmap(inputmap):
    for line in inputmap:
        print(''.join([str(i) for i in line]))

def basinsize(basinmap):
    return sum(sum(i for i in line if i == 1) for line in basinmap) 

basinsizes = []

printmap(heightmap)
for y in range(len(heightmap)):
    for x in range(len(heightmap[0])):
        if getheight(heightmap, x - 1, y) > heightmap[y][x] and \
           getheight(heightmap, x + 1, y) > heightmap[y][x] and \
           getheight(heightmap, x, y - 1) > heightmap[y][x] and \
           getheight(heightmap, x, y + 1) > heightmap[y][x]:
            # now floodfill
            floodfillmap = [[0] * len(heightmap[0]) for i in range(len(heightmap))]
            floodfillmap = fill(heightmap, floodfillmap, x, y)
            #printmap(floodfillmap)

            # add the basin size to the list
            basinsizes.append(basinsize(floodfillmap))

            print("Low point at: (" + str(x) + "," + str(y) + "): " + str(heightmap[y][x]) + " size: " + str(basinsize(floodfillmap)))

# sort the basin size list and get the 3 largest and multiply them together to get the answer
basinsizes.sort(reverse = True)

score = 1
for size in basinsizes[0:3]:
    score = score * size
print(score)
