
lines = open("input.1").read().splitlines()
lines = open("input.test").read().splitlines()
#lines = open("input.test2").read().splitlines()
#lines = open("input.test3").read().splitlines()


paths = {}
smallcaves = []

for line in lines:
    path = line.split("-")
    
    # add path based on startpoint
    if not(path[0] in paths.keys()):
        paths[path[0]] = []
    paths[path[0]].append(path[1])

    # add path based on endpoint
    if not(path[1] in paths.keys()):
        paths[path[1]] = []
    paths[path[1]].append(path[0])

    # identify small caves
    if path[0].islower() and not(path[0] in smallcaves):
        smallcaves.append(path[0])
    if path[1].islower() and not(path[1] in smallcaves):
        smallcaves.append(path[1])

def inlist(l, s):
    for i in range(len(l) - 1):
        if s == l[i:i+2]:
            return True
    return False

def findpaths(paths, path, startpoint):
    solutions = []
    for endpoint in paths[startpoint]:
        temppath = path.copy()
        if endpoint == "end":
            temppath.append(endpoint)
            print(temppath)
            solutions.append(temppath)
        if endpoint != "start" and not(inlist(temppath, [startpoint, endpoint])) and \
           not(endpoint in temppath and endpoint in smallcaves):
            temppath.append(endpoint)
            solutions += findpaths(paths, temppath, endpoint)
    return solutions


solution = []
solution = findpaths(paths, ["start"], "start")

#print(solution)
print(len(solution))
