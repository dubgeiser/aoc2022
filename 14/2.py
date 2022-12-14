#!/usr/bin/env python3


def draw_line(pfrom, pto, blocking):
    blocking.add(pfrom)
    blocking.add(pto)
    ppx, ppy = pfrom
    epx, epy = pto
    if ppx == epx:
        y1, y2 = (ppy, epy) if ppy <= epy else (epy, ppy)
        for y in range(y1, y2):
            blocking.add((ppx, y))
    elif ppy == epy:
        x1, x2 = (ppx, epx) if ppx <= epx else (epx, ppx)
        for x in range(x1, x2):
            blocking.add((x, ppy))


def fill_with_sand(origin, blocking, max_depth):
    ox, oy = origin
    while oy <= max_depth:
        # "I keep on faaaallin'..."
        if (ox, oy + 1) not in blocking:
            oy += 1
            continue
        # "To the left, to the left..."
        if (ox - 1, oy + 1) not in blocking:
            ox -= 1
            oy += 1
            continue
        # "To the right, to the right..." Is this a song?
        if (ox + 1, oy +1) not in blocking:
            ox += 1
            oy += 1
            continue
        break
    # Final endpoint of the sand
    return (ox, oy)


with open("input") as data:
    paths = [l.strip() for l in data.read().strip().split("\n")]
blocking = set()
for path in paths:
    path_data = path.split(" -> ")
    pfrom = None
    for p_data in path_data:
        pto = tuple(map(int, p_data.split(",")))
        if pfrom is None:
            pfrom = pto
            continue
        draw_line(pfrom, pto, blocking)
        pfrom = pto

sand_origin = (500, 0)
max_depth = max([p[1] for p in blocking])
answer = 0
while True:
    end_point = fill_with_sand(sand_origin, blocking, max_depth)
    blocking.add(end_point)
    answer += 1
    if end_point == sand_origin:
        break

print()
print(f"{answer = }")
