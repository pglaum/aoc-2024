#!/usr/bin/env python3
import math
import os.path
import sys
from pprint import pprint

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/..')

from aoc import get_lines

lines = get_lines('input')
nums = [int(x) for x in lines[0]]

fs = []
is_file = True
file_id = 0
for num in nums:
    if is_file:
        for i in range(num):
            fs.append(file_id)
        file_id += 1
    else:
        for i in range(num):
            fs.append(-1)

    is_file = not is_file

end_idx = len(fs) - 1

new_fs = []
for i, f in enumerate(fs):
    if i > end_idx:
        break

    if f == -1:
        while fs[end_idx] == -1:
            end_idx -= 1
        if end_idx <= i:
            break
        new_fs.append(fs[end_idx])
        end_idx -= 1
    else:
        new_fs.append(f)

#print(', '.join([str(x) for x in new_fs]))
checksum = 0
for i, f in enumerate(new_fs):
    if f == -1:
        continue
    checksum += i * f

print('part1:', checksum)


fs = {}
is_file = True
file_id = 0
space_id = -1
idx = 0
for i, num in enumerate(nums):
    if is_file:
        fs[idx] = (True, num, file_id)
        file_id += 1
    else:
        fs[idx] = (False, num, -1)

    idx += num
    is_file = not is_file

#print('parsed:')
#pprint(fs)
#print()

def print_fs(fs):
    new_str = ''
    keys = sorted(fs.keys())
    for k in keys:
        v = fs[k]
        for j in range(v[1]):
            if v[0]:
                new_str += str(v[2])
            else:
                new_str += '.'
    print(new_str)


def merge_fs(fs):
    new_fs = fs.copy()
    checked_keys = []
    done = False
    idx = 0
    while not done:
        idx += 1
        done = True
        keys = sorted(new_fs.keys())
        for k in reversed(keys):
            v = new_fs[k]
            if v[0] and k not in checked_keys:
                keys2 = sorted(new_fs.keys())
                for k2 in keys2:
                    if k2 == k:
                        break

                    v2 = new_fs[k2]
                    if not v2[0] and v2[1] >= v[1]:
                        if v2[1] == v[1]:
                            new_fs[k2] = (True, v2[1], v[2])
                        else:
                            new_fs[k2 + v[1]] = (False, v2[1] - v[1], -1)
                            new_fs[k2] = (True, v[1], v[2])
                        new_fs[k] = (False, v[1], -1)
                        break
                checked_keys.append(k)
                done = False
                break
        #print_fs(new_fs)
        if idx % 1000 == 0:
            print('iteration:', idx)

    return new_fs

nfs = merge_fs(fs)

# print('merged:')
# pprint(nfs)

checksum = 0
i = 0
for k in sorted(nfs.keys()):
    v = nfs[k]
    for j in range(v[1]):
        if v[0]:
            checksum += i * v[2]
        i += 1

print('part2:', checksum)