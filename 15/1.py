#!/usr/bin/env python3

import re
import sys


sample="""Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3"""


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


regex_coord = r"x=(-?\d+), y=(-?\d+)"
regex = re.compile(f"Sensor at {regex_coord}: closest beacon is at {regex_coord}")
sensors = []
beacons = []
distances = []
with open("input") as data:
    lines = [l.strip() for l in data]
    for l in lines:
        sx, sy, bx, by = map(int, regex.findall(l)[0])
        sensors.append((sx, sy))
        beacons.append((bx, by))
        distances.append(abs(sx - bx) + abs(sy - by))
Y_TARGET = 2000000
y_coverage = []
x_min = sys.maxsize
x_max = -x_min
for i, s in enumerate(sensors):
    sx, sy = s
    dtarget = abs(sy - Y_TARGET)

    # No need to calculate further if we can't even reach target y axis.
    if distances[i] < dtarget: continue

    dx = distances[i] - dtarget
    x_left = sx - dx
    x_right = sx + dx
    x_min = min(x_left, x_min)
    x_max = max(x_right, x_max)
    y_coverage.append((x_left, x_right))

# following the puzzle example; beacons on Y_TARGET are valid positions to put
# a beacon (Now that I'm writing this... UHU
# Keep track of the beacons on Y_TARGET
free_x = set([bx for bx, by in beacons if by == Y_TARGET])

answer = 0
# Go through outer most left side on Y_TARGET and outer most right side and
# check if we have detected coverage on Y_TARGET (ie. a beacon cannot be present)
for x in range(x_min, x_max + 1):
    if x in free_x: continue # beacons on Y_TARGET
    for xl, xr in y_coverage:
        if x >= xl and x <= xr:
            answer += 1
            break

print(f"{answer = }")
