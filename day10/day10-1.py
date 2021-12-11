# https://adventofcode.com/2021/day/10 

import os

currentWorkingDir = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(currentWorkingDir + '\exampleinput.txt') as f:
    lines = f.readlines()

# https://www.geeksforgeeks.org/stack-in-python/

penalty = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

sets = {
    '(': ')',
    '{': '}',
    '[': ']',
    '<': '>',
}
openers = sets.keys()
closers = sets.values()
score = 0

for line in lines:
    stack = []
    for char in list(line.strip()):
        if char in openers:
            stack.append(char)

        elif char in closers:
            should_match = stack.pop()

            if char != sets[should_match]:
                print(f"Expected {sets[should_match]}, but found {char} instead.")

                score += penalty[char]

                break
        else:
            print("invalid thingy found, '{char}'".format(char=char))

print(score)

