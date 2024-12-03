#!/usr/bin/env python3

import os.path
import sys

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/..')

from aoc import get_line_arrays_from_file

reports = get_line_arrays_from_file('input', ' ', True)


def is_safe(report):
    last_num = report[0]
    inc = False
    for i in range(1, len(report)):
        if report[i] == last_num:
            return 0
        if abs(report[i] - last_num) > 3:
            return 0
        if i == 1:
            inc = report[i] > last_num
        else:
            if inc and report[i] <= last_num:
                return 0
            if not inc and report[i] >= last_num:
                return 0
        last_num = report[i]

    return 1


def part1(reports):
    valid = 0
    for report in reports:
        valid += is_safe(report)

    print('part1:', valid)


def part2(reports):
    valid = 0
    for report in reports:
        its_safe = is_safe(report)
        if its_safe == 0:
            for i in range(len(report)):
                rep = report[:i] + report[i+1:]
                its_safe = is_safe(rep)
                if its_safe == 1:
                    break

        valid += its_safe

    print('part2:', valid)


part1(reports)
part2(reports)