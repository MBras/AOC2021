cave = [list(line) for line in open("input.t1").read().splitlines()]
#cave = [list(line) for line in open("input.t2").read().splitlines()]
cave = [list(line) for line in open("input.p").read().splitlines()]

h = len(cave)
w = len(cave[0])

def pc(c): # print cave
    print("\n".join("".join(line) for line in c))

print("Initial state:")
pc(cave)

counter = 1
while True:
    # initialize new situation
    tempcave1 = [["."] * w for i in range(h)]
    tempcave2 = [["."] * w for i in range(h)]

    # move east
    for x in range(w):
        for y in range(h):
            if cave[y][x] == ">":
                # check if x + 1 is free
                if cave[y][(x + 1) % w] == ".":
                    tempcave1[y][(x + 1) % w] = ">"
                else:
                    tempcave1[y][x] = ">"
            elif cave[y][x] == "v":
               tempcave1[y][x] = "v" 

    # mvoe down
    for x in range(w):
        for y in range(h):
            if tempcave1[y][x] == "v":
                # check if y + 1 is free
                if tempcave1[(y + 1) % h][x] == ".":
                    tempcave2[(y + 1) % h][x] = "v"
                else:
                    tempcave2[y][x] = "v"
            elif tempcave1[y][x] == ">":
                tempcave2[y][x] = ">"
                
    print(f"\nAfter {counter} steps:")
    pc(tempcave2)

    if tempcave2 == cave:
        print("\nEverything stopped moving")
        break

    counter += 1

    cave = tempcave2
