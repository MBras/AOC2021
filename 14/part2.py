from collections import Counter

[template, temprules] = open("input.test").read().split("\n\n")
[template, temprules] = open("input.1").read().split("\n\n")

rules = {}
for rule in temprules.splitlines():
    rules[rule.split(" -> ")[0]] = rule.split(" -> ")[1]

steps = 40

print("Template: " + template)

checklist = [template[i: i + 2] for i in range(len(template) - 1)]
count_cl = Counter(checklist)

for step in range(steps):
    #print("step: " + str(step + 1))
    #print(count_cl)
    new_ccl = {}
    for combo in count_cl:
        newchar = rules[combo]

        left = combo[0] + newchar
        right = newchar + combo[1]

        try:
            new_ccl[left] += count_cl[combo] 
        except:
            new_ccl[left] = count_cl[combo]
        try:    
            new_ccl[right] += count_cl[combo]
        except:
            new_ccl[right] = count_cl[combo]

    count_cl = new_ccl

result = {}
for combo in count_cl:
    left = combo[0]
    right = combo[1]
    try:
        result[left] += count_cl[combo]
    except:
        result[left] = count_cl[combo]
    try:
        result[right] += count_cl[combo]
    except:
        result[right] = count_cl[combo]

# compensate for the fact that the first and last character only appear once ever
result[template[0]] += 1
result[template[-1]] += 1

# now divide all values by 2 as everything appears twice
result = [result[i] // 2 for i in result]

print(max(result) - min(result))
