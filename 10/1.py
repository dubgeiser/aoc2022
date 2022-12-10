#!/usr/bin/env python3

def is_important(cycle: int) -> bool:
    return cycle in [20, 60, 100, 140, 180, 220]


with open("input") as data:
    program = [l.strip() for l in data]

x = 1
cycle = 0
answer = 0

for instruction in program:
    cycle += 1
    if is_important(cycle):
        answer += cycle * x
    if instruction.startswith("addx "):
        cycle += 1
        if is_important(cycle):
            answer += cycle * x
        v = int(instruction.replace("addx ", ""))
        x += v

print(f"{answer = }")
