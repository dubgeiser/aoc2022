#!/usr/bin/env python3


def read_data_file(fn):
    with open(fn) as data:
        sacks = []
        for l in data:
            # Since we are comparing over sacks, we can make each sack a set.
            sacks.append(set([c for c in l.strip()]))
    return sacks


def solve(data):
    priorities = [c for c in 'abcdefghijklmnopqrstuvwxyz'] + [C for C in  'ABCDEFGHIJKLMNOPQRSTUVWXYZ']
    elves_per_group = 3
    answer = 0
    for i in range(elves_per_group - 1, len(data), elves_per_group):
        answer += priorities.index(list(data[i].intersection(data[i - 1], data[i - 2]))[0]) + 1
    return answer


if __name__ == "__main__":
    answer = solve(read_data_file("input"))
    print(f"{answer = }")
