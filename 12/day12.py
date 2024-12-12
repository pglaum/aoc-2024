#!/usr/bin/env python3
import functools
from math import log10, ceil
import os.path
import sys
from pprint import pprint

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/..')
sys.setrecursionlimit(10000)

from aoc import get_lines

lines = get_lines('input')
lines = [lines.strip() for lines in lines]

directions = [
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0),
]
sdirs = {
    (0, 1): '>',
    (1, 0): 'v',
    (0, -1): '<',
    (-1, 0): '^',
}
def find_area(area: list[tuple[int, int]], plant: str, pos: tuple[int, int]):
    for d in directions:
        npos = (pos[0] + d[0], pos[1] + d[1])
        if npos[0] < 0 or npos[1] < 0:
            continue
        if npos[0] >= len(lines) or npos[1] >= len(lines[0]):
            continue

        if npos not in area and lines[npos[0]][npos[1]] == plant:
            area.append(npos)
            area = find_area(area, plant, npos)

    return area

def find_edges_and_sides(area: list[tuple[int, int]]):
    edges = []
    sides = {}
    for a in area:
        for d in directions:
            npos = (a[0] + d[0], a[1] + d[1])
            if npos not in area:
                edges.append(a)
                if d[1] == 0:
                    skey = f"{sdirs[d]}_{npos[0]}"
                    if skey not in sides:
                        sides[skey] = []
                    sides[skey].append(npos[1])
                else:
                    skey = f"{sdirs[d]}_{npos[1]}"
                    if skey not in sides:
                        sides[skey] = []
                    sides[skey].append(npos[0])

    return edges, sides

def find_connected_sides(sides):
    count = 0
    for k in sides:
        values = sorted(sides[k])
        if len(values) == 0:
            continue

        count += 1
        for i in range(1, len(values)):
            if abs(values[i] - values[i - 1]) > 1:
                count += 1
    return count

visited = []
score = 0
score2 = 0
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if (i, j) in visited:
            continue

        area = find_area([(i, j)], lines[i][j], (i, j))
        edges, sides = find_edges_and_sides(area)
        count = find_connected_sides(sides)

        print(lines[i][j], len(area), len(edges), count)
        score += len(area) * len(edges)
        score2 += len(area) * count
        visited.extend(area)

print('part1:', score)
print('part2:', score2)