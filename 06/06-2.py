#!/usr/bin/env python3


BUFSIZE = 14


def read_data_file(fn):
    with open(fn) as data:
        stream = list(data.read().strip())
    return stream


def is_unique(buffer):
    return len(buffer) == len(set(buffer))


def solve(data):
    i = 0
    while True:
        if is_unique(data[i:i + BUFSIZE]):
            return i + BUFSIZE
        i += 1


if __name__ == "__main__":
    answer = solve(read_data_file("input"))
    print(f"{answer = }")

