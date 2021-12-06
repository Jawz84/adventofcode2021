# https://adventofcode.com/2021/day/6 

import os

currentWorkingDir = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(currentWorkingDir + '\exampleinput.txt') as f:
    lines = f.readlines()

lantarnFish = list(map(int, lines[0].split(',')))

days = 0
while days < 256:
    for l in range(0, len(lantarnFish)):
        if lantarnFish[l] == 0:
            lantarnFish[l] = 6
            lantarnFish.append(8)
        else:
            lantarnFish[l] -= 1
    days += 1

print(len(lantarnFish))

