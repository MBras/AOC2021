[algo, timage] = open("input.test").read().split("\n\n")
[algo, timage] = open("input.t2").read().split("\n\n")
[algo, timage] = open("input.1").read().split("\n\n")

# process algorithm data
algo = ["0" if a == "." else "1" for a in list(algo)]

# process image data and add a extra empty square around the image
extra = 0 
timage = timage.splitlines()
image = [["0"] * (len(timage[0]) + 2 * extra) for i in range(len(timage) + 2 * extra)]

for x in range(len(timage[0])):
    for y in range(len(timage)):
        image[y + extra][x + extra] = "0" if timage[y][x] == "." else "1"

print(algo)
print('\n'.join(''.join("#" if i == "1" else "." for i in line) for line in image))

def getval(x, y, i, step):
    #print("checking ("+str(x)+","+str(y)+")")
    if 0 <= x < len(i[0]) and 0 <= y < len(i):
        return i[y][x]
    else:
        if algo[0] == "1":
            return "0" if (step % 2 == 0) else "1"
        else:
            return "0"

# enhance
def enhance(image, step):
    # create temp image
    timage = [["0"] * (len(image[0]) + 2) for i in range(len(image) + 2)]

    # for every pixel enhance
    for y in range(len(timage)):
        for x in range(len(timage[0])):
            # get the surrounding values
            ai = ""
            for yy in range(y - 2, y + 1):
                for xx in range(x - 2, x + 1):
                    ai += getval(xx, yy, image, step)
            #print("Algorithm input for ("+str(x)+","+str(y)+"): " + ai + " - " + str(int(ai, 2)) + ": " +  algo[int(ai,2)])
            timage[y][x] = algo[int(ai,2)]

    print('\n'.join(''.join("#" if i == "1" else "." for i in line) for line in timage))
    return timage

for s in range(50):
    print("After enhance " + str(s))
    image = enhance(image, s)
print("Day 20, part 2: " + str(sum(sum(1 if i == "1" else 0 for i in line) for line in image)))
