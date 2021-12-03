# https://adventofcode.com/2021/day/3 

import os
from typing import List

currentWorkingDir = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(currentWorkingDir + '\input.txt') as f:
    lines = f.readlines()

orig_lines = lines.copy()


for i in range(0, (len(lines[0]))):
    indices_high = []
    indices_low = []

    for j in range(0, len(lines)-1):
        if (lines[j] == '\n'):
            continue
        if lines[j][i] == '1':
            indices_high.append(j)
        else:
            indices_low.append(j)

    if len(indices_high) >= len(indices_low):
        for j in range((len(indices_low))-1, -1, -1):
            lines.pop(indices_low[j])
    else:
        for j in range((len(indices_high))-1, -1, -1):
            lines.pop(indices_high[j])

    if len(lines) == 2:
        break

print("oxygen:")
oxygen = int(lines[0], 2)
print(lines[0].strip())
print(oxygen)

lines = orig_lines

for i in range(0, (len(lines[0]))):
    indices_high = []
    indices_low = []

    for j in range(0, len(lines)-1):
        if (lines[j] == '\n'):
            continue
        if lines[j][i] == '1':
            indices_high.append(j)
        else:
            indices_low.append(j)

    if len(indices_high) < len(indices_low):
        for j in range((len(indices_low))-1, -1, -1):
            lines.pop(indices_low[j])
    else:
        for j in range((len(indices_high))-1, -1, -1):
            lines.pop(indices_high[j])

    if len(lines) == 2:
        break

print("co2:")
print(lines[0].strip())
print(int(lines[0], 2))

life_support = int(lines[0], 2) * oxygen

print("life support:")
print(life_support)

