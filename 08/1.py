#!/usr/bin/env python3


with open("input") as data:
    map = [[int(n) for n in l.strip()] for l in data]

SIZE_ROW = len(map)
SIZE_COL = len(map[0])
VISIBLE = set()

def check_horizontal(row: int, col: int):
    height = map[row][col]
    return all(map[row][c] < height for c in range(col)) or all(map[row][c] < height for c in range(col + 1, SIZE_COL))


def check_vertical(row: int, col: int):
    height = map[row][col]
    return all(map[r][col] < height for r in range(row)) or all(map[r][col] < height for r in range(row + 1, SIZE_ROW))

def check_visibilty(row: int, col: int) -> bool:
    return check_horizontal(row, col) or check_vertical(row, col)

answer = 0
for row in range(0, SIZE_ROW):
    for col in range(0, SIZE_COL):
        if check_visibilty(row, col):
            VISIBLE.add((row, col))

answer += len(VISIBLE)
print(f"{answer = }")
