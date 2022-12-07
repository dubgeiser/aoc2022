#!/usr/bin/env python3


def read_data_file(fn):
    max = 0
    current_total = 0
    with open(fn) as data:
        for line in data:
            if line.strip() == '':
                if current_total > max:
                    max = current_total
                current_total = 0
                continue
            current_total += int(line.strip())
    return max


def solve(data):
    return data


if __name__ == "__main__":
    answer = solve(read_data_file("input"))
    print(f"{answer = }")
