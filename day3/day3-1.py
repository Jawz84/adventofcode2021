# https://adventofcode.com/2021/day/3 

import os

currentWorkingDir = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(currentWorkingDir + '\input.txt') as f:
    lines = f.readlines()

gamma_rate = [0] * (len(lines[0])-1)
epsilon_rate = [0] * (len(lines[0])-1)

code = [0] * (len(lines[0])-1)

for binary in lines:
    i = 0
    for bit in list(binary):
        if bit == '1':
            code[i] += 1
        i += 1

half = (len(lines) -2) / 2


for i in range(0, len(code)):
    if code[i] > half:
        gamma_rate[i] = 1
        epsilon_rate[i] = 0
    else:
        gamma_rate[i] = 0
        epsilon_rate[i] = 1

gamma_rate = ''.join(map(str,gamma_rate))
epsilon_rate = ''.join(map(str,epsilon_rate))

print(gamma_rate)
print(epsilon_rate)

print(int(gamma_rate, 2))
print(int(epsilon_rate, 2))

print(int(gamma_rate, 2) * int(epsilon_rate, 2))

