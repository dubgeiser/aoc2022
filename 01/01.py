#!/usr/bin/env python3


def read_data_file(fn):
    totals = []
    current_total = 0
    with open(fn) as data:
        for line in data:
            if line.strip() == '':
                totals.append(current_total)
                current_total = 0
                continue
            current_total += int(line.strip())
    # Don't forget the last one!
    totals.append(current_total)
    return totals


def solve(data):
    data.sort()
    print(f"{data = }")
    return data[-3] + data[-2] + data[-1]


if __name__ == "__main__":
    answer = solve(read_data_file("input"))
    print(f"{answer = }")
