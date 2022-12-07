#!/usr/bin/env python3


def read_data_file(fn):
    with open(fn) as data:
        lines = [l.strip() for l in data]
    return lines


def solve(data):
    priorities = [c for c in 'abcdefghijklmnopqrstuvwxyz'] + [C for C in  'ABCDEFGHIJKLMNOPQRSTUVWXYZ']
    answer = 0
    for l in data:
        half = int(len(l) / 2)
        c1 = [c for c in l[0:half]]
        c2 = [c for c in l[half:len(l)]]
        found = False
        for c in c1:
            if c in c2:
                found = True
                answer += priorities.index(c) + 1
                break
            if found:
                break
    return answer


if __name__ == "__main__":
    answer = solve(read_data_file("input"))
    print(f"{answer = }")
