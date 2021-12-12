# https://adventofcode.com/2021/day/9 

import os
import time

currentWorkingDir = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(currentWorkingDir + '\input.txt') as f:
    lines = f.readlines()

def get_above(coordinate):
    x, y = coordinate
    return 9 if y==0 else Map[y-1][x] # handle top of map by returning 9

def findIndex(coordinate):
    for i in range(0, len(SetList)):
        if {coordinate}.issubset(SetList[i]):
            return i

Map = [list(map(int, list(x.strip()))) for x in lines]
SetList = []

# put all coordinates into a set
for y in range(0, len(Map)):
    prev = 9 # handle left edge of map by setting to 9 each new row
    for x in range(0, len(Map[0])):
        curr = Map[y][x]
        above = get_above((x,y))

        # skip all 9s
        if curr == 9:
            prev = 9
            continue

        indexOfSetBefore = findIndex((x-1,y))
        indexOfSetAbove = findIndex((x,y-1))

        if prev == 9 and above == 9:
            # unconnected field, new set
            SetList.append({(x,y)})
        elif above == 9:
            SetList[indexOfSetBefore].add((x,y))
        elif prev == 9:
            SetList[indexOfSetAbove].add((x,y))
        elif indexOfSetAbove != indexOfSetBefore:
            # merge sets if we end up finding a connection of two sets
            SetList[indexOfSetAbove].add((x,y))
            setToAddToOtherSet = SetList[indexOfSetBefore]
            SetList[indexOfSetAbove].update(setToAddToOtherSet)
            SetList.pop(indexOfSetBefore) # pop after update to avoid indexing error
        else:
            SetList[indexOfSetAbove].add((x,y))

        prev = curr

# get the largest three sets
SetList.sort(key=len, reverse=True)
size = len(SetList[0]) * len(SetList[1]) * len(SetList[2])
print(size)

