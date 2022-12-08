#!/usr/bin/env python3


with open("input") as data:
    print()
    print(sum(sorted([sum(g) for g in [
        map(int, g.splitlines()) for g in data.read().split("\n\n")]])[-3:]))
