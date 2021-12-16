# read cave
input = [[int(i) for i in list(line)] for line in open("input.test").read().splitlines()]
input = [[int(i) for i in list(line)] for line in open("input.2").read().splitlines()]
#input = [[int(i) for i in list(line)] for line in open("input.1").read().splitlines()]
print('\n'.join(''.join(str(i) for i in line) for line in input))

# height and width of the input
w = len(input[0])
h = len(input)

c = [[0] * w * 5 for i in range(h * 5)]
# fill the cave for part 2
for yy in range(5):
    for y in range(h):
        for xx in range(5):
            for x in range(w):
                c[xx * w + x][yy * h + y] = (input[x][y] + xx + yy - 1) % 9 + 1

# height and width of the cave (often used)
w = len(c[0])
h = len(c)

# display cave
print('\n'.join(''.join(str(i) for i in line) for line in c))

# movement directions 
md = [[0,-1],[0,1],[-1,0],[1,0]]

# N for non visited nodes, l for the least risky path, v for the least risky connected node
N =[] 
l = {}
v = {}
for x in range(w):
    for y in range(h):
        N.append([x,y])
        l[x,y]= h * w * 9
        v[x,y] = None

# visited nodes
B = []

# current starting node
cur = [0,0]
l[cur[0],cur[1]] = 0 

B.append(cur)
# while not all nodes have been done
while len(N) > 0:
    # visit all neighbours for current node
    
    for direction in md:
        # determine neighnour node coordinate
        x = cur[0] + direction[0] 
        y = cur[1] + direction[1]

        # check if the coordinates are within the cave and not done yet
        if [x,y] in N and 0 <= x < w and 0 <= y < h:
            d = l[cur[0],cur[1]] + c[x][y]
            # check if the new distance is less than current distance
            if d < l[x,y]:
                # lesser distance, update lists
                l[x,y] = d
                v[x,y] = cur
            B.append([x,y])
    
    # remove current node from N
    N.remove(cur)
    B.remove(cur)

    # set new current node
    # keep track of values for the new start node
    sp = h * w * 9
    spc = None
    print(B)
    for node in B:
        if l[node[0],node[1]] < sp:
            sp = l[node[0],node[1]]
            spc = node
    print(cur)
    cur = spc

    print("Percentage complete: " + str(round(100 - (len(N)/(h*w) * 100), 2)) + "%")

#print("N:")
#print(N)
#print("B:")
#print(B)
#print("l:")
#print(l)
#print("v:")
#print(v)
#print("current node:")
#print(cur)

print(l[w - 1, h - 1])
