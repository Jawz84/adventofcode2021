# https://adventofcode.com/2021/day/4 

import os

currentWorkingDir = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(currentWorkingDir + '\input.txt') as f:
    lines = f.readlines()

def __has_row_bingo(card):
    for i in range(0, 5):
        if sum(card[i]) == -5:
            return True
    return False

def __has_column_bingo(card):
    for i in range(0, 5):
        if sum([row[i] for row in card]) == -5:
            return True
    return False

def __cross_off_draw_row(row, draw):
    return [-1 if x==draw else x for x in row]

def __sum_non_negative_values(row):
    return sum(x for x in row if x >= 0)

def get_card_row(line):
    return list(map(int, line.replace('  ',' ').strip().split(' ')))

def has_bingo(card):
    return __has_row_bingo(card) or __has_column_bingo(card)

def cross_off_draw(card, draw):
    return [__cross_off_draw_row(row, draw) for row in card]

def sum_non_negative_values(card):
    return sum(__sum_non_negative_values(row) for row in card)

# read numbers to draw
numbers_to_draw = lines[0].strip().split(',')
numbers_to_draw = [int(x) for x in numbers_to_draw]

# read all bingo cards
bingo_cards = []
for i in range(2, len(lines)-2, 6):
    # store bingo card as a list of lists [5 * 5]
    card = [
        get_card_row(lines[i]),
        get_card_row(lines[i + 1]),
        get_card_row(lines[i + 2]),
        get_card_row(lines[i + 3]),
        get_card_row(lines[i + 4])
    ]
    bingo_cards.append(card)

# foreach number to draw, handle all bingo cards
for draw in numbers_to_draw:
    # cross off the number
    bingo_cards = [cross_off_draw(card, draw) for card in bingo_cards]

    # if we stil have cards left, and a card has bingo, remove it from the list
    if len(bingo_cards) > 1:
        bingo_cards = [card for card in bingo_cards if not has_bingo(card)]
    else:
        if has_bingo(bingo_cards[0]):
            print(sum_non_negative_values(bingo_cards[0]) * draw)
            exit()
