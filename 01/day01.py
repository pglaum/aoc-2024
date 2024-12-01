#!/usr/bin/env python3

with open('input') as f:
    content = f.readlines()

line1 = [int(x.split('   ')[0]) for x in content]
line2 = [int(x.split('   ')[1]) for x in content]

line1sorted = sorted(line1, key=lambda x: x)
line2sorted = sorted(line2, key=lambda x: x)

add = 0
for i in range(len(line1sorted)):
    add += abs(line1sorted[i] - line2sorted[i])

print('1 - result:', add)

add = 0
for num in line1:
    count = line2.count(num)
    add += num * count

print('2 - result:', add)