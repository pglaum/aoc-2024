#!/usr/bin/env python3
import math
import os.path
import sys
from pprint import pprint

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/..')

from aoc import get_lines

lines = get_lines('input')

antennas = {}

for i, line in enumerate(lines):
    for j, c in enumerate(line):
        if c == '\n':
            continue

        if c != '.':
            if c not in antennas:
                antennas[c] = []
            antennas[c].append((i, j))

antinodes = []
for fk in antennas:
    f = antennas[fk]
    added = 0
    for i in range(0, len(f) - 1):
        for j in range(i + 1, len(f)):
            dline = abs(f[i][0] - f[j][0])
            dcol = abs(f[i][1] - f[j][1])

            l1 = f[i][0] - dline
            l2 = f[j][0] + dline

            if f[i][1] < f[j][1]:
                c1 = f[i][1] - dcol
                c2 = f[j][1] + dcol
            else:
                c1 = f[i][1] + dcol
                c2 = f[j][1] - dcol

            if l1 >= 0 and l1 < len(lines) and c1 >= 0 and c1 < len(lines[0]) - 1:
                added += 1
                antinodes.append((l1, c1))


            if l2 >= 0 and l2 < len(lines) and c2 >= 0 and c2 < len(lines[0]) - 1:
                added += 1
                antinodes.append((l2, c2))

print('part1:', len(set(antinodes)))

antinodes = []

for fk in antennas:
    f = antennas[fk]
    added = 0
    for i in range(0, len(f) - 1):
        for j in range(i + 1, len(f)):
            dline = abs(f[i][0] - f[j][0])
            dcol = abs(f[i][1] - f[j][1])

            antinodes.append(f[i])
            antinodes.append(f[j])

            out_of_bounds1 = False
            out_of_bounds2 = False
            k = 1
            while not out_of_bounds1 or not out_of_bounds2:
                l1 = f[i][0] - int(dline * k)
                l2 = f[j][0] + int(dline * k)

                if f[i][1] < f[j][1]:
                    c1 = f[i][1] - int(dcol * k)
                    c2 = f[j][1] + int(dcol * k)
                else:
                    c1 = f[i][1] + int(dcol * k)
                    c2 = f[j][1] - int(dcol * k)

                if l1 >= 0 and l1 < len(lines) and c1 >= 0 and c1 < len(lines[0]) - 1:
                    antinodes.append((l1, c1))
                else:
                    out_of_bounds1 = True

                if l2 >= 0 and l2 < len(lines) and c2 >= 0 and c2 < len(lines[0]) - 1:
                    antinodes.append((l2, c2))
                else:
                    out_of_bounds2 = True

                k += 1

print('part2:', len(set(antinodes)))