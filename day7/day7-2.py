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

listPositions = [[key, crabsAtPosition[key]] for key in crabsAtPosition]

fuelPerPosition = []

def getSumOfAscendingSequence(end):
    return (end * (end + 1)) // 2

for i in range(0, max(positions)+1):
    fuel = 0
    for j in range(0, len(crabsAtPosition)):
        fuel += getSumOfAscendingSequence(abs(i - listPositions[j][0])) * listPositions[j][1]
    fuelPerPosition.append([i, fuel])

# get smallest distance in distances
fuelPerPosition.sort(key=lambda x: x[1])

print(fuelPerPosition[0])