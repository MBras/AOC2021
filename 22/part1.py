import re

input = open("input.t1").read()
#input = open("input.t2").read()
#input = open("input.t3").read()
#input = open("input.p").read()

regexp = "(on|off) x=(-?\d*)..(-?\d*),y=(-?\d*)..(-?\d*),z=(-?\d*)..(-?\d*)"
matches = re.findall(regexp, input)

cubes = {}

minv = -50
maxv = 50

for match in matches:
    print(match)
    #print("Turning " +  match[0] + ": ")
    for x in range(int(match[1]), int(match[2]) + 1):
        if minv <= x <= maxv:
            for y in range(int(match[3]), int(match[4]) + 1):
                if minv <= y <= maxv:
                    for z in range(int(match[5]), int(match[6]) + 1):
                        if minv <= z <= maxv:
                            if match[0] == "on":
                                if x not in cubes.keys():
                                    cubes[x] = {}
                                if y not in cubes[x].keys():
                                    cubes[x][y] = {}
                                if z not in cubes[x][y].keys():
                                    cubes[x][y][z] = 1
                                    #print(str(x) + "," + str(y) + "," + str(z))
                                else:
                                    #print("Already on: " + str(x) + "," + str(y) + "," + str(z))
                                    pass
                            else:
                                try:
                                    del cubes[x][y][z]
                                except:
                                    pass


for x in cubes:
    for y in cubes[x]:
        for z in cubes[x][y]:
            #print(str(x) + "," + str(y) + "," + str(z))
            pass
print(sum(sum(sum(x for x in y.values()) for y in z.values()) for z in cubes.values()))
