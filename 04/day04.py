#!/usr/bin/env python3

import os.path
import re
import sys

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/..')

from aoc import get_lines

lines = get_lines('input')

matrix = [
    [[-1, -1], [-2, -2], [-3, -3]], # top left
    [[-1, 0], [-2, 0], [-3, 0]], # top
    [[-1, 1], [-2, 2], [-3, 3]], # top right
    [[0, -1], [0, -2], [0, -3]], # left
    [[0, 1], [0, 2], [0, 3]], # right
    [[1, -1], [2, -2], [3, -3]], # bottom left
    [[1, 0], [2, 0], [3, 0]], # bottom
    [[1, 1], [2, 2], [3, 3]], # bottom right
]

def find_xmas(lines, line, char):
    count = 0
    for direction in matrix:
        chars = 'MAS'
        has_word = True
        for i in range(0, len(direction)):
            nline = line + direction[i][0]
            nchar = char + direction[i][1]

            if nline < 0 or nline >= len(lines) or nchar < 0 or nchar >= len(lines[nline]):
                has_word = False
                break

            if lines[nline][nchar] == chars[i]:
                continue

            has_word = False

        if has_word:
            count += 1

    return count


xmas = 0

for i, line in enumerate(lines):
    for j, char in enumerate(line):
        if char == 'X':
            xmas += find_xmas(lines, i, j)


print('part1:', xmas)

def find_x_mas(lines, line, char):
    if line - 1 < 0 or char - 1 < 0 or line + 1 >= len(lines) or char + 1 >= len(lines[line]):
        return 0

    matches = []
    matches.append(lines[line - 1][char - 1])
    matches.append(lines[line - 1][char + 1])
    matches.append(lines[line + 1][char - 1])
    matches.append(lines[line + 1][char + 1])
    matches = [x for x in matches if x in ['M', 'S']]

    if len(matches) != 4:
        return 0

    if matches.count('M') != 2 or matches.count('S') != 2:
        return 0

    if matches[0] == matches[3] or matches[1] == matches[2]:
        return 0

    return 1

xmas = 0
for i, line in enumerate(lines):
    for j, char in enumerate(line):
        if char == 'A':
            xmas += find_x_mas(lines, i, j)

print('part2:', xmas)