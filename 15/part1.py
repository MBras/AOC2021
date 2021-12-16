import sys
sys.setrecursionlimit(100000)

# read cave
c = [[int(i) for i in list(line)] for line in open("input.test").read().splitlines()]
#c = [[int(i) for i in list(line)] for line in open("input.2").read().splitlines()]
c = [[int(i) for i in list(line)] for line in open("input.1").read().splitlines()]

# height and width of the cave (often used)
w = len(c[0])
h = len(c)

# display cave
print('\n'.join(''.join(str(i) for i in line) for line in c))

# movement directions 
md = [[0,-1],[0,1],[-1,0],[1,0]]

# non visited nodes, l for the least risky path, v for the least risky connected node
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

# while not all nodes have been done
while len(N) > 0:
    # visit all neighbours for current node
    
    for direction in md:
        # determine neighnour node coordinate
        x = cur[0] + direction[0] 
        y = cur[1] + direction[1]

        # check if the coordinates are within the cave
        if 0 <= x < w and 0 <= y < h and [x,y] in N:
            d = l[cur[0],cur[1]] + c[x][y]
            # check if the new distance is less than current distance
            if d < l[x,y]:
                # lesser distance, update lists
                l[x,y] = d
                v[x,y] = cur
    
    # move cur from N to B
    N.remove(cur)
    B.append(cur)

    # set new current node
    # keep track of values for the new start node
    sp = h * w * 9
    spc = None
    for node in N:
        if l[node[0],node[1]] < sp:
            sp = l[node[0],node[1]]
            spc = node
    cur = spc

print("N:")
print(N)
print("B:")
print(B)
print("l:")
print(l)
print("v:")
print(v)
print("current node:")
print(cur)

print(l[w - 1, h - 1])
