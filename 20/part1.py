[algo, timage] = open("input.test").read().split("\n\n")
[algo, timage] = open("input.1").read().split("\n\n")

# process algorithm data
algo = ["0" if a == "." else "1" for a in list(algo)]

# process image data and add a extra empty square around the image
timage = timage.splitlines()
image = [["0"] * (len(timage[0]) + 4) for i in range(len(timage) + 4)]

for x in range(len(timage[0])):
    for y in range(len(timage)):
        image[y + 2][x + 2] = "0" if timage[y][x] == "." else "1"

print(algo)
print('\n'.join(''.join("#" if i == "1" else "." for i in line) for line in image))

# enhance
def enhance(image):
    # create temp image
    timage = [["0"] * (len(image[0]) + 2) for i in range(len(image) + 2)]

    # for every pixel enhance
    for y in range(1, len(image) - 1):
        for x in range(1, len(image[0]) - 1):
            # get the surrounding values
            ai = ""
            for yy in range(y - 1, y + 2):
                ai += "".join(image[yy][x - 1: x + 2])
            #print("Algorithm input for ("+str(x)+","+str(y)+"): " + ai + " - " + str(int(ai, 2)) + ": " +  algo[int(ai,2)])
            timage[y + 1][x + 1] = algo[int(ai,2)]

    print('\n'.join(''.join("#" if i == "1" else "." for i in line) for line in timage))
    return timage

print("After first enhance:")
image = enhance(image)
print("After second enchance:")
image = enhance(image)

print(sum(sum(1 if i == "1" else 0 for i in line) for line in image))
