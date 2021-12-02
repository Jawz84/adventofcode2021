# https://adventofcode.com/2021/day/2 

import os

currentWorkingDir = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(currentWorkingDir + '\input.txt') as f:
    lines = f.readlines()

distance = 0
depth = 0

for command in lines:
    if command == '\n':
        continue
    c = command.split(' ')
    action = c[0] 
    amount = c[1]

    if action == 'forward':
        distance += int(amount)
    elif action == 'up':
        depth -= int(amount)
    elif action == 'down':
        depth += int(amount)
    
print(distance * depth)




