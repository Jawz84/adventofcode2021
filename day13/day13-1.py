# https://adventofcode.com/2021/day/13 

import os

currentWorkingDir = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(currentWorkingDir + '\input.txt') as f:
    lines = f.readlines()

Points = [(int(line.split(',')[0]), int(line.split(',')[1])) for line in lines if line != '\n' and not line.startswith('fold')]
folds = [(line.split('=')[0].split(' ')[-1], int(line.split('=')[1])) for line in lines if line.startswith('fold')]

def print_points():
    os.system('cls')
    for point in Points:
        print (f"\033[{point[1]+1};{point[0]+1}HX")
    print("\033[16;0H\n")

# folds are exactly halving the size of the paper each time

for fold in folds[0:1]:
    if fold[0] == 'x':
        xFold = fold[1]
        pointsToRemove = []
        for point in Points:

            if point[0] > xFold:
                temp = (xFold - (point[0] - xFold), point[1])
                if temp not in Points:
                    Points.append(temp)
                pointsToRemove.append(point)

        for point in pointsToRemove:
            Points.remove(point)

    elif fold[0] == 'y':
        yFold = fold[1]
        pointsToRemove = []
        for point in Points:
            if point[1] > yFold:
                temp = (point[0], yFold - (point[1] - yFold))
                if temp not in Points:
                    Points.append(temp)
                pointsToRemove.append(point)

        for point in pointsToRemove:
            Points.remove(point)

# print_points()
print(len(Points))