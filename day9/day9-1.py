# https://adventofcode.com/2021/day/9 

import os

currentWorkingDir = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(currentWorkingDir + '\input.txt') as f:
    lines = f.readlines()

Map = [list(map(int, list(x.strip()))) for x in lines]


def hasLowerNeighbours(x, y):
    if y == 0:
        above = 10
    else:
        above = Map[y - 1][x]

    if y == len(Map) - 1:
        below = 10
    else:
        below = Map[y + 1][x]

    if x == 0:
        left = 10
    else:
        left = Map[y][x - 1]

    if x == len(Map[0]) - 1:
        right = 10
    else:
        right = Map[y][x + 1]


    if Map[y][x] < below and Map[y][x] < above and Map[y][x] < left and Map[y][x] < right:
        return False
    else:
        return True



lowPoints = []
for y in range(0, len(Map)):
    for x in range(0, len(Map[0])):
        if not hasLowerNeighbours(x, y):
            lowPoints.append([(x, y), Map[y][x]])


# sum of all the (low points + 1) -> risklevel
print(sum([x[1] + 1 for x in lowPoints]))