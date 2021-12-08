# https://adventofcode.com/2021/day/8 

import os

currentWorkingDir = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(currentWorkingDir + '\input.txt') as f:
    lines = f.readlines()

count =0
for line in lines:
    for x in line.split('|')[1].strip().split(' '):
        if len(x) == 2 or len(x) == 3 or len(x) == 4 or len(x) == 7:
            count += 1

print(count)