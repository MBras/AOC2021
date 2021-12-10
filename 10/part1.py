lines = open("input.1").read()
#lines = open("input.test").read()
lines = [list(line) for line in lines.splitlines()]

start = ["(","{","[","<"]
end = [")","}","]",">"]
match = {"(" : ")", "{" : "}", "[" : "]", "<" : ">"} 
charscore = {")": 3, "}": 1197,"]": 57,">": 25137}

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
                return(charscore[char])
    return 0

score = 0

print(sum(checkline(line) for line in lines))
