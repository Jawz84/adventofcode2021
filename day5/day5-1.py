# https://adventofcode.com/2021/day/5 

import os

currentWorkingDir = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(currentWorkingDir + '\input.txt') as f:
    lines = f.readlines()

class cloud:
    def __init__(self, line):
        self.start = [int(x) for x in (line.strip().split(" -> ")[0].split(","))]
        self.end = [int(x) for x in (line.strip().split(" -> ")[1].split(","))]

    def __str__(self):
        return f'{self.start} -> {self.end}'

    def get_all_coordinates(self):
        if self.start[0] == self.end[0]:
            if self.start[1] < self.end[1]:
                return [(self.start[0], y) for y in range(self.start[1], self.end[1]+1)]
            else:
                return [(self.start[0], y) for y in range(self.end[1], self.start[1]+1)]
        elif self.start[1] == self.end[1]:
            if self.start[0] < self.end[0]:
                return [(x, self.start[1]) for x in range(self.start[0], self.end[0]+1)]
            else:
                return [(x, self.start[1]) for x in range(self.end[0], self.start[0]+1)]

clouds = [cloud(line) for line in lines]

cloudCoords = []

for c in clouds:
    if c.start[0] == c.end[0] or c.start[1] == c.end[1]:
        cloudCoords += c.get_all_coordinates()


field = [0]*1000
for i in range(0, len(field)):
    field[i] = [0]*1000

count = 0
for coord in cloudCoords:
    if field[coord[1]][coord[0]] == 0:
        field[coord[1]][coord[0]] = 1
    elif field[coord[1]][coord[0]] == 1:
        field[coord[1]][coord[0]] = 2
        count +=1

# for row in field:
#     print(row)

print (count)

