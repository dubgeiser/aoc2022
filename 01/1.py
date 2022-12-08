#!/usr/bin/env python3


with open("input") as data:
    print()
    print(max([sum(g) for g in [
        map(int, g.splitlines()) for g in data.read().split("\n\n")]]))
