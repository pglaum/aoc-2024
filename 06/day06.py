#!/usr/bin/env python3

import os.path
import sys

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/..')

from aoc import get_lines

content = get_lines('input')

pos = []
visited = []
directions = [
    [-1, 0],
    [0, 1],
    [1, 0],
    [0, -1]
]
direction_idx = 0
obstacles = []

def get_starter():
    for i in range(len(content)):
        for j in range(len(content[i])):
            if content[i][j] == '^':
                return [i, j]

def get_next():
    global direction_idx
    global pos

    direction = directions[direction_idx]
    new_pos = [pos[0] + direction[0], pos[1] + direction[1]]
    if new_pos[0] < 0 or new_pos[0] >= len(content) or new_pos[1] < 0 or new_pos[1] >= len(content[0]):
        return -1

    if content[new_pos[0]][new_pos[1]] == '#':
        direction_idx = (direction_idx + 1) % 4
        return 1

    pos = new_pos

    visited.append([pos, directions[direction_idx]])
    return 0

pos = get_starter()
visited.append([pos, directions[direction_idx]])

while True:
    res = get_next()
    if res == -1:
        break

visited_set = set(map(tuple, [x[0] for x in visited]))

print('part1:', len(visited_set))


def get_next_with_loop(the_map):
    global direction_idx
    global pos

    direction = directions[direction_idx]
    new_pos = [pos[0] + direction[0], pos[1] + direction[1]]
    if new_pos[0] < 0 or new_pos[0] >= len(the_map) or new_pos[1] < 0 or new_pos[1] >= len(the_map[0]):
        return -1

    if the_map[new_pos[0]][new_pos[1]] == '#':
        direction_idx = (direction_idx + 1) % 4
        return 1

    pos = new_pos

    # try obstacle
    for v in visited:
        if v[0] == pos and v[1] == direction_idx:
            # loop
            return -2

    visited.append([pos, direction_idx])
    return 0


old_visited = [x[0] for x in visited]
obstacles = []
for i in range(len(content)):
    for j in range(len(content[i])):
        if content[i][j] == '#':
            continue

        if [i, j] not in old_visited:
            continue

        obstacle = [i, j]

        pos = get_starter()
        if pos == [i, j]:
            continue
        direction_idx = 0
        visited = []
        visited.append([pos, direction_idx])

        the_map = content.copy()
        the_map[i] = the_map[i][:j] + '#' + the_map[i][j + 1:]
        while True:
            res = get_next_with_loop(the_map)
            if res == -1:
                print('obstacle not found:', obstacle)
                break
            if res == -2:
                obstacles.append(obstacle)
                print('obstacle found:', obstacle)
                break

print('part2:', len(obstacles))