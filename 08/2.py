#!/usr/bin/env python3


with open("input") as data:
    map = [[int(n) for n in l.strip()] for l in data]

SIZE_ROW = len(map)
SIZE_COL = len(map[0])


def visible_left(row: int, col: int) -> int:
    count = 0
    height = map[row][col]
    for c in range(col - 1, -1, -1):
        count += 1
        if map[row][c] >= height:
            break
    return count


def visible_right(row:int, col: int) -> int:
    count = 0
    height = map[row][col]
    for c in range(col + 1, SIZE_COL):
        count += 1
        if map[row][c] >= height:
            break
    return count


def visible_up(row:int, col: int) -> int:
    count = 0
    height = map[row][col]
    for r in range(row - 1, -1, -1):
        count += 1
        if map[r][col] >= height:
            break
    return count


def visible_down(row:int, col: int) -> int:
    count = 0
    height = map[row][col]
    for r in range(row + 1, SIZE_ROW):
        count += 1
        if map[r][col] >= height:
            break
    return count


answer = 0
for row in range(0, SIZE_ROW):
    for col in range(0, SIZE_COL):
        total = visible_left(row, col) * visible_right(row, col) * visible_up(row, col) * visible_down(row, col)
        answer = max(answer, total)
print(f"{answer = }")
