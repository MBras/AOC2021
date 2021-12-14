from collections import Counter

[template, temprules] = open("input.test").read().split("\n\n")
[template, temprules] = open("input.1").read().split("\n\n")

rules = {}
for rule in temprules.splitlines():
    rules[rule.split(" -> ")[0]] = rule.split(" -> ")[1]
print(rules)
steps = 10

print("Template: " + template)

for step in range(steps):
    polymer = ""
    for i in range(len(template) - 1):
        polymer += template[i]
        polymer += rules[template[i: i + 2]]

    polymer += template[-1]
    
    print("After step " + str(step + 1) + ": " + polymer)

    template = polymer

counter = Counter(list(polymer))
print(max(counter.values()) - min((counter.values())))
