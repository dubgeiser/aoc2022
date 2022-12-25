#!/usr/bin/env python3

import re


"""
Y = 10
sensor: (8, 7), distance: 9 (beacon not needed... yet)
coverage as function of sx, sy, distance and Y
y = 7:  dx: -1,17   -> (sx - ?, sx + ?)
y = 8:  dx: 0, 16   -> (sx - ?, sx + ?)
y = 9:  dx: 1, 15   -> (sx - ?, sx + ?)
y = 10: dx: 2, 14   -> (sx - ?, sx + ?)

? = distance - |sy - Y|
"""


def merge_intervals(intervals):
    x1 = 0
    x2 = 1
    last = -1
    sorted_intervals = sorted(intervals)
    merged = []
    merged.append(sorted_intervals[0])
    for i in sorted_intervals[1:]:
        if merged[last][x1] <= i[x1] <= merged[last][x2]:
            merged[last][x2] = max(merged[last][x2], i[x2])
        else:
            merged.append(i)
    return merged


regex_coord = r"x=(-?\d+), y=(-?\d+)"
regex = re.compile(f"Sensor at {regex_coord}: closest beacon is at {regex_coord}")
sensors = []
distances = []
with open("input") as data:
    lines = [l.strip() for l in data]
    for l in lines:
        sx, sy, bx, by = map(int, regex.findall(l)[0])
        sensors.append((sx, sy))
        distances.append(abs(sx - bx) + abs(sy - by))

Y_TARGET = 2000000
intervals = []
for i, s in enumerate(sensors):
    sx, sy = s
    dtarget = abs(sy - Y_TARGET)

    # No need to calculate further if we can't even reach target y axis.
    if distances[i] < dtarget: continue

    dx = distances[i] - dtarget
    x_left = sx - dx
    x_right = sx + dx
    intervals.append([x_left, x_right])

answer = sum([abs(x2 - x1) for x1, x2 in merge_intervals(intervals)])
print(f"{answer = }")
