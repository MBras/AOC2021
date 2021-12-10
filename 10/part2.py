lines = open("input.1").read()
#lines = open("input.test").read()
lines = [list(line) for line in lines.splitlines()]

start = ["(","{","[","<"]
end = [")","}","]",">"]
match = {"(" : ")", "{" : "}", "[" : "]", "<" : ">"} 
charscore = {")": 3, "}": 1197,"]": 57,">": 25137}
charscore2 = {"(": 1, "[": 2, "{": 3,"<": 4}

def checkline(line):
    lastchar = []
    for char in line:
        # check if a startinf character
        if char in start:
            lastchar.append(char)
        
        # check if an ending character
        if char in end:
            # check if it matches the current starting character
            if char == match[lastchar[-1]]:
                lastchar.pop()
            else:
                print("".join(line) + " - Expected " + match[lastchar[-1]] + ", but found " + char + " instead.")
                return None
    return lastchar

def scoreline(line):
    s = 0
    line.reverse()
    for char in line:
        s = s * 5 + charscore2[char]
    return s

score = 0

remaininglines = []

for line in lines:
    remaininglines.append(checkline(line))
remaininglines = [line for line in remaininglines if line]

scores = [scoreline(line) for line in remaininglines]
scores.sort()

print(scores[len(scores)//2])
