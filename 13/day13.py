#!/usr/bin/env python3
import functools
from math import log10, ceil
import os.path
import sys
from pprint import pprint

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/..')
sys.setrecursionlimit(10000)

from aoc import get_lines, get_content

content = get_content('input')

add = 10000000000000

class Machine:
    def __init__(self, button_a, button_b, prize):
        self.A = button_a
        self.B = button_b
        self.prize = prize
        self.lowest_cost = -1
        self.lowest_cost_at = (0, 0)
        self.lowest_cost_2 = -1

    def print(self):
        print(f'A: {self.A}, B: {self.B}, Prize: {self.prize}, Lowest cost: {self.lowest_cost}, Lowest cost at: {self.lowest_cost_at}, Lowest cost 2: {self.lowest_cost_2}')

    def get_cost(self):
        tries = ceil(self.prize[0] / min(self.A[0], self.A[1]))
        for i in range(tries):
            p1 = self.prize[0] - i * self.A[0]
            if p1 % self.B[0] == 0:
                j = p1 // self.B[0]
                if i * self.A[1] + j * self.B[1] == self.prize[1]:
                    cost = i * 3 + j
                    if self.lowest_cost == -1 or cost < self.lowest_cost:
                        self.lowest_cost = cost
                        self.lowest_cost_at = (i, j)

    def get_high_prize(self):
        return self.prize[0] + add, self.prize[1] + add

    def get_cost_2(self):
        # ax*a + bx*b = tx
        # ay*a + by*b = ty
        # b = (tx*ay - ty*ax) / (ay*bx - by*ax)
        # a = (tx*by - ty*bx) / (by*ax - bx*ay)
        ax, ay = self.A
        bx, by = self.B
        tx, ty = self.get_high_prize()
        b = (tx*ay - ty*ax) // (ay*bx - by*ax)
        a = (tx*by - ty*bx) // (by*ax - bx*ay)

        if ax * a + bx * b == tx and ay * a + by * b == ty:
            self.lowest_cost_2 = 3 * a + b

        return


machine_lines = content.split('\n\n')
machines = []

for ml in machine_lines:
    lines = ml.splitlines()
    a1 = lines[0].split('X+')[1].split(',')[0]
    a2 = lines[0].split('Y+')[1]
    b1 = lines[1].split('X+')[1].split(',')[0]
    b2 = lines[1].split('Y+')[1]
    p1 = lines[2].split('X=')[1].split(',')[0]
    p2 = lines[2].split('Y=')[1]

    machines.append(Machine((int(a1), int(a2)), (int(b1), int(b2)), (int(p1), int(p2))))

part1 = 0
part2 = 0
for m in machines:
    m.get_cost()
    if m.lowest_cost != -1:
        part1 += m.lowest_cost

    m.get_cost_2()
    if m.lowest_cost_2 != -1:
        part2 += m.lowest_cost_2

    m.print()

print('part1:', part1)
print('part2:', part2)