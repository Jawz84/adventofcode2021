# https://adventofcode.com/2021/day/8 

import os

currentWorkingDir = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(currentWorkingDir + '\input.txt') as f:
    lines = f.readlines()

# I was completely stuck on this one, so I went to the subreddit for a hint, and I found one on a scrap of paper that struck the chord and here we are:

sum = 0
for line in lines:
    # get all codes and identify all 1, 4, 7 and 8 values
    codes = []
    for x in line.strip().split(' '):
        if x == '|':
            continue

        # When we find a 1 or a 4, we save these as sets to compare later
        if len(x) == 2:
            one = set(list(x))
            codes.append([x, 1])
        if len(x) == 4:
            four = set(list(x))
            codes.append([x, 4])
        if len(x) == 3:
            codes.append([x, 7])
        if len(x) == 7:
            codes.append([x, 8])
        if len(x) == 5:
            codes.append([x, -1])
        if len(x) == 6:
            codes.append([x, -2])

    # This figure is the L-shape of the 4, and is an extra piece of hidden information.
    fourDiff = four - one

    # Now that we know the one, four and the L-shape, we can compare those to the codes
    for code in codes:
        if code[1] >= 0:
            continue
        current = set(list(code[0]))
        if code[1] == -1: # length is 5, so number is 2, 3 or 5
            if one.issubset(current):
                code[1] = 3
            elif fourDiff.issubset(current):
                code[1] = 5
            else:
                code[1] = 2
        if code[1] == -2: # length is 6, so number is 0, 6 or 9
            if four.issubset(current):
                code[1] = 9
            elif fourDiff.issubset(current):
                code[1] = 6
            else:
                code[1] = 0

    # The last four items in the list of Codes are the ones after the '|'. 
    # They need to become one single number, so multiply them per position with their magnitude and add up.
    number = codes[10][1]*1000 + codes[11][1]*100 + codes[12][1]*10 + codes[13][1]
    sum += number
    #print (number)

print (sum)