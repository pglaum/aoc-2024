#!/usr/bin/env python3

import os.path
import re
import sys

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/..')

from aoc import get_lines

content = '\n'.join(get_lines('input'))

comp = re.compile(r'mul\((\d+),(\d+)\)')
groups = comp.findall(content)
result = 0
for group in groups:
    result += (int(group[0]) * int(group[1]))

print('part1:', result)

last_do = 0
i = 0
string = ''
dont = False
while True:
    if i >= len(content):
        break

    if dont and content[i:].startswith('do()'):
        dont = False
        i += 4
        last_do = i
        continue

    if not dont and content[i:].startswith("don't()"):
        string += content[last_do:i]
        dont = True
        i += 7
        continue

    i += 1

if not dont:
    string += content[last_do:]

print(string)
comp = re.compile(r'mul\((\d+),(\d+)\)')
groups = comp.findall(string)
result = 0
for group in groups:
    result += (int(group[0]) * int(group[1]))

print('part2:', result)