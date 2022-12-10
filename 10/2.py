#!/usr/bin/env python3


with open("input") as data:
    program = [l.strip() for l in data]

x = 1
cycle = 0
# Hold the occupied positions of the sprite (on the X-axis) during each cycle.
sprite_positions = []
screen = [["." for _ in range(40)] for _ in range(6)]

for instruction in program:
    cycle += 1
    sprite_positions.append((x - 1, x, x + 1))
    if instruction.startswith("addx "):
        cycle += 1
        sprite_positions.append((x - 1, x, x + 1))
        v = int(instruction.replace("addx ", ""))
        x += v

cycle = 0
for row in range(len(screen)):
    for x in range(len(screen[0])):
        if x in sprite_positions[cycle]:
            # Storing 2 chars, otherwise I can't read the damn thing!
            screen[row][x] = "##"
        else:
            screen[row][x] = "  "
        cycle += 1

print()
for row in range(len(screen)):
    print()
    for x in range(len(screen[0])):
        print(screen[row][x], end="")
