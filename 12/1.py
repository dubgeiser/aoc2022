#!/usr/bin/env python3

from collections import defaultdict
import heapq
from string import ascii_lowercase


def mkheightmap(map):
    """ Make the given map (with letters) a heightmap.
    S -> start point with height 0
    E -> end point with height 25
    a -> 0
    z -> 25
    """
    start = end = (-1, -1)
    for row in range(len(map)):
        for col in range(len(map[0])):
            if map[row][col] == "S":
                start = (row, col)
                map[row][col] = ascii_lowercase.index('a')
            elif map[row][col] == "E":
                end = (row, col)
                map[row][col] = ascii_lowercase.index('z')
            else:
                map[row][col] = ascii_lowercase.index(map[row][col])
    return start, end


def valid_neighbors(map, row, col):
    max_row = len(map) - 1
    max_col = len(map[0]) - 1
    """ Generator for finding all the neighbors of a given position in a given map. """
    for row_move, col_move in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        next_row = row + row_move
        next_col = col + col_move
        if next_row > max_row or next_row < 0 or next_col > max_col or next_col < 0:
            continue
        # Can only move to neighbor if it's 1 higher, same height or whatever lower
        if map[next_row][next_col] <= map[row][col] + 1:
            yield next_row, next_col


with open("input") as data:
    map = [list(l.strip()) for l in data]

start, end = mkheightmap(map)
visited = set()
pq = [(0, start[0], start[1])]
steps = -1
heapq.heapify(pq)
while len(pq) > 0:
    steps, row, col = heapq.heappop(pq)
    if (row, col) in visited:
        continue
    visited.add((row, col))
    if (row, col) == end: break
    for nrow, ncol in valid_neighbors(map, row, col):
        heapq.heappush(pq, (steps + 1, nrow, ncol))

print()
print(steps)
