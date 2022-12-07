#!/usr/bin/env python3

import re


def parse_crates(raw):
    # Use last crate number to determine our regex.
    cratenrs = int(raw.pop().strip()[-1])
    r = re.compile("^" + "(.{3}) " * (cratenrs - 1) + "(.{3})$")
    crates = [[]]
    raw.reverse()
    for l in raw:
        crateline = r.findall(l)[0]
        for i, c in enumerate(crateline):
            if c.strip() == '':
                continue
            if i >= len(crates):
                crates.append([])
            crates[i].append(c.replace('[', '').replace(']', ''))
    return crates


def parse_moves(raw):
    # 1 line -> move 15 from 7 to 1
    moves = []
    for l in raw:
        _, amount, _, src, _, dest = l.split(" ")
        # make src and destination list indices
        moves.append((int(amount), int(src) - 1, int(dest) - 1))
    return moves


def read_data_file(fn):
    crates_raw, moves_raw = open(fn).read().split("\n\n")
    crates_raw = crates_raw.split("\n")
    moves_raw = moves_raw.strip().split("\n")
    crates = parse_crates(crates_raw)
    moves = parse_moves(moves_raw)
    return (crates, moves)


def solve(data):
    crates, moves = data
    for amount, src, dest in moves:
        tmp = []
        for _ in range(0, amount):
            tmp.append(crates[src].pop())
        tmp.reverse()
        crates[dest] += tmp
    answer = ''
    for each in crates:
        answer += each.pop()
    return answer


if __name__ == "__main__":
    answer = solve(read_data_file("input"))
    print(f"{answer = }")
