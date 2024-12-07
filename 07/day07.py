#!/usr/bin/env python3

import os.path
import sys

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/..')

from aoc import get_lines

lines = get_lines('input')

def find_true_eval(target: int, numbers: list[int]):
    if len(numbers) == 2:
        return numbers[0] + numbers[1] == target or numbers[0] * numbers[1] == target

    mediate = numbers[0] + numbers[1]
    if mediate <= target and find_true_eval(target, [mediate] + numbers[2:]):
        return True

    mediate = numbers[0] * numbers[1]
    if mediate <= target and find_true_eval(target, [mediate] + numbers[2:]):
        return True

    return False


def find_true_eval2(target: int, numbers: list[int]):
    if len(numbers) == 2:
        return numbers[0] + numbers[1] == target or \
            numbers[0] * numbers[1] == target or \
            int(f"{numbers[0]}{numbers[1]}") == target

    mediate = numbers[0] + numbers[1]
    if mediate <= target and find_true_eval2(target, [mediate] + numbers[2:]):
        return True

    mediate = numbers[0] * numbers[1]
    if mediate <= target and find_true_eval2(target, [mediate] + numbers[2:]):
        return True

    mediate = int(f"{numbers[0]}{numbers[1]}")
    if mediate <= target and find_true_eval2(target, [mediate] + numbers[2:]):
        return True

    return False

res = 0
res2 = 0
for line in lines:
    result = int(line.split(':')[0])
    numbers = list(map(int, line.split(':')[1].split()))
    if find_true_eval(result, numbers):
        res += result

    if find_true_eval2(result, numbers):
        print('TRUE', result, numbers)
        res2 += result
    else:
        print('FALSE', result, numbers)

print('part1:', res)
print('part2:', res2)