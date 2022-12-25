#!/usr/bin/env python3

import re


"""
Algo:
go through all y's from 0 -> target
if we find 2 intervals instead of 1 and i2[x1] does not come right after i1[x2]
we've found it at (i2[x1] - 1, y) if i2[x1] - 1 <= target
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


def find_intervals_on_y(y: int, sensors: list[tuple[int,int]]):
    intervals = []
    for i, s in enumerate(sensors):
        sx, sy = s
        dtarget = abs(sy - y)

        # No need to calculate further if we can't even reach target y axis.
        if distances[i] < dtarget: continue

        dx = distances[i] - dtarget
        x_left = sx - dx
        x_right = sx + dx
        intervals.append([x_left, x_right])
    return merge_intervals(intervals)


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

TARGET = 4000000
answer = 0
for y in range(0, TARGET):
    intervals = find_intervals_on_y(y, sensors)
    if len(intervals) == 1: continue
    elif intervals[0][1] + 1 == intervals[1][0]: continue
    elif intervals[1][0] > TARGET: continue
    else:
        x = intervals[1][0] - 1
        break

answer = x * 4000000 + y
print()
print(f"{answer = }")
