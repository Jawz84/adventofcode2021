# https://adventofcode.com/2021/day/10 

import os

currentWorkingDir = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(currentWorkingDir + '\input-ron.txt') as f:
    lines = f.readlines()

# https://www.geeksforgeeks.org/stack-in-python/

score_dict = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

sets = {
    '(': ')',
    '{': '}',
    '[': ']',
    '<': '>',
}
openers = sets.keys()
closers = sets.values()
scores = []

for line in lines:
    stack = []
    skip_score = False
    for char in list(line.strip()):
        if char in openers:
            stack.append(char)

        elif char in closers:
            should_match = stack.pop()

            if char != sets[should_match]:
                # print(f"Expected {sets[should_match]}, but found {char} instead.")
                skip_score = True
                break
        else:
            print("invalid thingy found, '{char}'".format(char=char))

    if not skip_score:
        score = 0
        stack.reverse()
        for item in stack:
            matching_closer = sets[item]
            score *= 5
            score += score_dict[matching_closer]
        scores.append(score)
 
scores.sort()
print(scores[len(scores)//2])

