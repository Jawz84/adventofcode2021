# https://adventofcode.com/2021/day/7 

import os

currentWorkingDir = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(currentWorkingDir + '\input.txt') as f:
    lines = f.readlines()

positions = list(map(int, lines[0].strip().split(',')))
positions.sort()
median = positions[len(positions) // 2]

crabsAtPosition = {}
for pos in positions:
    crabsAtPosition.update({pos: crabsAtPosition[pos] + 1 if pos in crabsAtPosition else 1})

distance = 0
for pos in crabsAtPosition:
    distance += abs(median - pos) * crabsAtPosition[pos]

print(distance)