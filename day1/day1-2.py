import os

currentWorkingDir = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(currentWorkingDir + '\input.txt') as f:
    lines = f.readlines()

sum = 0

for i in range(len(lines)-4):
    measure1 = int(lines[i]) + int(lines[i+1]) + int(lines[i+2])
    measure2 = int(lines[i+1]) + int(lines[i+2]) + int(lines[i+3])
    if (measure1 < measure2):
        sum += 1

print(sum)