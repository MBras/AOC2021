import sys
sys.setrecursionlimit(100000)

# read cave
c = [[int(i) for i in list(line)] for line in open("input.test").read().splitlines()]
c = [[int(i) for i in list(line)] for line in open("input.2").read().splitlines()]
#c = [[int(i) for i in list(line)] for line in open("input.1").read().splitlines()]

# height and width of the cave (often used)
w = len(c[0])
h = len(c)

# initialize lowest risk path map
lr = [[h * w * 9] * w for i in range(h)]

# movement directions
md = [[-1, 0],[1,0],[0,-1],[0,1]]

# recursive function which find the least risky path from location (x,y)
def findpath(x, y):
    print("Checking (" + str(x) + "," + str(y) + ") ")
    # for current location, check all surrounding location
    for d in md:
        cx = x + d[0]
        cy = y + d[1]
        if 0 <= cx < w and 0 <= cy < h:
            print("Checking (" + str(x) + "," + str(y) + "): risk: " + str(c[x][y]) + " total risk: " + str(lr[x][y]))
            print(" against (" + str(cx) + "," + str(cy) + "): risk: " + str(c[cx][cy]) + " total risk: " + str(lr[cx][cy]))
            # add the risk level for current location to the target location
            if lr[cx][cy] + c[x][y] < lr[x][y]:
                # if it is lower than current level 
                # fill current location with that value and stop
                print("New path is less risky, set (" + str(x) + "," + str(y) + ") to " + str(lr[cx][cy] + c[x][y]))
                lr[x][y] = lr[cx][cy] + c[x][y]
                print('\n'.join(' '.join(str(i) for i in line) for line in lr))
                findpath(x, y)
            elif lr[cx][cy] + c[x][y] == lr[x][y]:
                print("Equal risk, do nothing")
                print('\n'.join(' '.join(str(i) for i in line) for line in lr))
            elif lr[x][y] + c[cx][cy] < lr[cx][cy]:
                # fill surrounding location with new value 
                # and continue searching from there
                print("Current path is less risky, set (" + str(cx) + "," + str(cy) + ") to " + str(lr[x][y] + c[cx][cy]))
                lr[cx][cy] = lr[x][y] + c[cx][cy]
                print('\n'.join(' '.join(str(i) for i in line) for line in lr))
                findpath(cx, cy)
            else:
                print("No idea?!")

# initialize the startposition with the topleft value
lr[0][0] = c[0][0]

# and find the least risky path
findpath(0, 0)

# print the score
print(lr[-1][-1] - c[-1][-1])
