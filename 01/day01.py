#!/usr/bin/env python3

import os.path
import sys

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/..')

from aoc import get_columns_from_file

columns = get_columns_from_file('input', '   ', True)

with open('input') as f:
    content = f.readlines()

line1sorted = sorted(columns[0], key=lambda x: x)
line2sorted = sorted(columns[1], key=lambda x: x)

add = 0
for i in range(len(line1sorted)):
    add += abs(line1sorted[i] - line2sorted[i])

print('1 - result:', add)

add = 0
for num in columns[0]:
    count = columns[1].count(num)
    add += num * count

print('2 - result:', add)