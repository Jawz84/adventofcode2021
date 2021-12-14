# https://adventofcode.com/2021/day/14 

import os

currentWorkingDir = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(currentWorkingDir + '\input.txt') as f:
    lines = f.readlines()

template = lines[0].strip()

rules = [(line.split(' -> ')[0], line.split(' -> ')[1].strip()) for line in lines[2:]]

rules = dict(rules)

for step in range(1, 11):
    indicesToInsert = []
    for rule in rules:
        _ = [indicesToInsert.append((index+1, rules[rule])) for index in range(len(template)) if template.startswith(rule, index)]

    indicesToInsert.sort(reverse=True)
    for i in indicesToInsert:
        template = template[:i[0]] + i[1] + template[i[0]:]

counters = {}
polymer = list(template)
for char in polymer:
    if char in counters:
        counters[char] += 1
    else:
        counters[char] = 1

max = max(counters.values())
min = min(counters.values())

print(max-min)