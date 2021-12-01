import os

currentWorkingDir = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(currentWorkingDir + '\input.txt') as f:
    lines = f.readlines()

sum = 0

for i in range(len(lines)-2):
    if int(lines[i]) < int(lines[i+1]):
        sum += 1

print(sum)