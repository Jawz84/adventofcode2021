# https://adventofcode.com/2021/day/11 

import os

currentWorkingDir = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(currentWorkingDir + '\input.txt') as f:
    lines = f.readlines()

grid = [list(map(int, list(line.strip()))) for line in lines]

def print_grid(grid):
    for i in grid:
        print(''.join(list(map(str, i))))
    print ('')

def check_flash(i, j, flashes):
    if grid[i][j] > 9 and (i, j) not in flashes:
        flashes.append((i, j))
        if i > 0:
            grid[i-1][j] += 1
            check_flash(i-1, j, flashes)
        if i < len(grid)-1:
            grid[i+1][j] += 1
            check_flash(i+1, j, flashes)
        if j > 0:
            grid[i][j-1] += 1
            check_flash(i, j-1, flashes)
        if j < len(grid[i])-1:
            grid[i][j+1] += 1
            check_flash(i, j+1, flashes)
        if i > 0 and j > 0:
            grid[i-1][j-1] += 1
            check_flash(i-1, j-1, flashes)
        if i > 0 and j < len(grid[i])-1:
            grid[i-1][j+1] += 1
            check_flash(i-1, j+1, flashes)
        if i < len(grid)-1 and j > 0:
            grid[i+1][j-1] += 1
            check_flash(i+1, j-1, flashes)
        if i < len(grid)-1 and j < len(grid[i])-1:
            grid[i+1][j+1] += 1
            check_flash(i+1, j+1, flashes)
        grid[i][j] = 0
    return flashes

steps = range(1, 101)
flashes = []
for step in steps:
    flashed_this_step = []

    # increase each element in grid by 1
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            grid[i][j] += 1

    # if an element is greater than 9, it becomes 0 and any surrounding element increases by 1
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            flashed_this_step = check_flash(i, j, flashed_this_step)

    # set all flashed elements to 0
    for i in flashed_this_step:
        grid[i[0]][i[1]] = 0

    [flashes.append(flash) for flash in flashed_this_step]
    # print (f"After step {step}")
    # print(f"flashes this step: {len(flashed_this_step)}, total flashes: {len(flashes)}")
    # print_grid(grid)

print (f"Total flashes: {len(flashes)}")