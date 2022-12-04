#!/usr/bin/env python3


def read_data_file(fn):
    pairs = []
    with open(fn) as data:
        for l in data:
            l = l.strip()
            r1, r2 = l.split(",")
            id1, id2 = r1.split("-")
            id3, id4 = r2.split("-")
            pairs.append((set(range(int(id1), int(id2) + 1)), set(range(int(id3), int(id4) + 1))))
    return pairs


def solve(data):
    answer = 0
    for s1, s2 in data:
        common = s1.intersection(s2)
        if common == s1 or common == s2:
            answer += 1
    return answer


if __name__ == "__main__":
    answer = solve(read_data_file("input"))
    print(f"{answer = }")
