import re

input = "target area: x=20..30, y=-10..-5"     # test data
input = "target area: x=155..182, y=-117..-67" #puzzle data

# parse input to get target area
ta = [int(i) for i in re.findall("target area: x=(-?[\d]*)..(-?[\d]*), y=(-?[\d]*)..(-?[\d]*)", input)[0]]

maxheight = 0
counter = [] 
for x in range(1,1040):#ta[1]):
    for y in range (-200, 200):
        pos      = [0,0]
        speed    = [x, y]
        overshot = False
        height   = 0

        while True:
            # get new position
            pos[0] = pos[0] + speed[0]
            pos[1] = pos[1] + speed[1]

            # get new height
            height = max(height, pos[1])
            
            # get new x speed
            speed[0] = max(0, speed[0] - 1)

            # get new y speed
            speed[1] -= 1

            #print(pos)
            # check overshot
            if pos[0] > ta[1] or pos[1] < ta[2]:
                #print("Overshot")
                break

            # check done
            if (ta[0] <= pos[0] <= ta[1] and ta[3] >= pos[1] >= ta[2]):
                #print("Checking speed (" + str(x) + "," + str(y) + ")")
                #print("In target area, height: " + str(height))
                # get new max height
                maxheight = max(maxheight, height)
                counter.append([x,y])
                break
            
print("Max height: " + str(maxheight))
print("Options: " + str(len(counter)))
#counter.sort()
#print(counter)
