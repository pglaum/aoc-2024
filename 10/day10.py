#!/usr/bin/env python3
import math
import os.path
import sys
from pprint import pprint

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/..')

from aoc import get_lines

lines = get_lines('input')
tmap = [[int(x) for x in line.strip()] for line in lines]

trail_heads = []
for i in range(len(tmap)):
    for j in range(len(tmap[i])):
        if tmap[i][j] == 0:
            trail_heads.append((i, j))

directions = [
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0)
]

def pos_is_valid(tmap, pos):
    if pos[0] < 0 or pos[0] >= len(tmap) or pos[1] < 0 or pos[1] >= len(tmap[pos[0]]):
        return False

    return True

def find_paths(tmap, pos, peaks = []):
    cur_h = tmap[pos[0]][pos[1]]

    #print('')
    for d in directions:
        new_pos = (pos[0] + d[0], pos[1] + d[1])
        if not pos_is_valid(tmap, new_pos):
            continue

        new_h = tmap[new_pos[0]][new_pos[1]]
        if new_h == cur_h + 1:
            #print('new_pos:', new_pos, new_h)
            if new_h == 9:
                peaks.append(new_pos)
                continue

            find_paths(tmap, new_pos, peaks)

    return peaks

score = 0
for th in trail_heads:
    peaks = find_paths(tmap, th, [])
    score += len(set(peaks))

print('part1:', score)

# part2

score = 0
for th in trail_heads:
    peaks = find_paths(tmap, th, [])
    score += len(peaks)

print('part2:', score)