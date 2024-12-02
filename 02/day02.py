#!/usr/bin/env python3

with open('input', 'r') as f:
    lines = f.readlines()
    reports = []
    for line in lines:
        reports.append([int(x) for x in line.split(' ')])

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


def is_safe2(report):
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

def part2(reports):
    valid = 0
    for report in reports:
        its_safe = is_safe2(report)
        if its_safe == 0:
            for i in range(len(report)):
                rep = report[:i] + report[i+1:]
                its_safe = is_safe2(rep)
                if its_safe == 1:
                    break

        valid += its_safe

    print('part2:', valid)


part1(reports)
part2(reports)