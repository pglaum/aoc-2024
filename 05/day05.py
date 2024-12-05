#!/usr/bin/env python3

import os.path
import re
import sys
from functools import cmp_to_key
from math import floor

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/..')

from aoc import get_content

content = get_content('input')

rule_str = content.split('\n\n')[0].splitlines()
update_str = content.split('\n\n')[1].splitlines()

rules = [[int(y) for y in x.split('|')] for x in rule_str]
updates = [[int(y) for y in x.split(',')] for x in update_str]

def is_valid(update, i):
    apply_rules = [x for x in rules if x[0] == update[i]]

    for rule in apply_rules:
        num = rule[1]
        for j in range(0, i):
            if update[j] == num:
                return False

    return True


def compare(a, b):
    rule_a = [x for x in rules if x[0] == a and x[1] == b]
    rule_b = [x for x in rules if x[0] == b and x[1] == a]
    if len(rule_a) > 0:
        return 1
    if len(rule_b) > 0:
        return -1
    return 0


def sort_update(update):
    supdate = sorted(update, key=cmp_to_key(compare))
    return supdate[floor(len(supdate)/2)]


result = 0
result2 = 0
for update in updates:
    v = True
    for i, page in enumerate(update):
        valid = is_valid(update, i)
        if not valid:
            v = False
            result2 += sort_update(update)
            break

    result += update[floor(len(update)/2)] if v else 0

print('part1:', result)
print('part2:', result2)
