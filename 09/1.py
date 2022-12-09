#!/usr/bin/env python3

# Index in coordinate tuples.
X = 0
Y = 1


def is_touching(p1: tuple[int, int], p2: tuple[int, int]) -> bool:
    return abs(p1[X] - p2[X]) <= 1 and abs(p1[Y] - p2[Y]) <= 1


def follow(head: tuple[int, int], tail: tuple[int, int]) -> tuple[int, int]:
    if not is_touching(head, tail):
        dx = dy = 0

        # Determine the movement the tail should take:
        # The sign of the distance determines its movement along the axis, the
        # division with its absolute value makes sure it's only 1, since we're\
        # doing this step by step.
        if head[X] != tail[X]:
            dx = int((head[X] - tail[X]) / abs(head[X] - tail[X]))
        if head[Y] != tail[Y]:
            dy = int((head[Y] - tail[Y]) / abs(head[Y] - tail[Y]))

        tail = (tail[X] + dx, tail[Y] + dy)
    return tail


# Movement in (x, y) coordinates
movement = {'L': (-1, 0),
            'R': (1, 0),
            'U': (0, 1),
            'D': (0, -1)}


with open("input") as data:
    moves = [tuple(l.strip().split()) for l in data]
visited = set()
head = (0, 0)
tail = (0, 0)
visited.add(tail)
for direction, distance in moves:
    distance = int(distance)
    m = movement[direction]
    for _ in range(distance):
        head = (head[X] + m[X], head[Y] + m[Y])
        tail = follow(head, tail)
        visited.add(tail)
print()
print(len(visited))
