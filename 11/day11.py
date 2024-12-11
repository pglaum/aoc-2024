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

nums = [int(x) for x in lines[0].split(' ')]

def blink(stones):
    res = []
    for s in stones:
        if s == 0:
            res.append(1)
            continue

        digits = len(str(s))
        if digits % 2 == 0:
            res.append(int(str(s)[:int(digits/2)]))
            res.append(int(str(s)[int(digits/2):]))
            continue

        res.append(s * 2024)

    return res

idx = 0
while idx < 25:
    nums = blink(nums)
    idx += 1

print('part1:', len(nums))

all_stones = {}
nums = [int(x) for x in lines[0].split(' ')]
for num in nums:
    if num in all_stones:
        all_stones[num] += 1
    else:
        all_stones[num] = 1


def blink2():
    global all_stones
    keys = list(all_stones.keys())
    add_stones = {}
    for s in all_stones.keys():
        if all_stones[s] == 0:
            continue

        if s == 0:
            if 1 not in add_stones:
                add_stones[1] = 0
            add_stones[1] += all_stones[s]
        else:
            digits = len(str(s))
            if digits % 2 == 0:
                if int(str(s)[:int(digits/2)]) not in add_stones:
                    add_stones[int(str(s)[:int(digits/2)])] = 0
                if int(str(s)[int(digits/2):]) not in add_stones:
                    add_stones[int(str(s)[int(digits/2):])] = 0

                add_stones[int(str(s)[:int(digits/2)])] += all_stones[s]
                add_stones[int(str(s)[int(digits/2):])] += all_stones[s]
            else:
                x2024 = int(s * 2024)
                if x2024 not in add_stones:
                    add_stones[x2024] = 0
                add_stones[x2024] += all_stones[s]


    all_stones = add_stones

#print(all_stones)
idx = 0
while idx < 75:
    blink2()
    idx += 1
    #print([x for x in all_stones.items() if x[1] > 0])

print('part2:', sum(all_stones.values()))