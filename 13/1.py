#!/usr/bin/env python3


PACKET_ORDER_CORRECT = 1
PACKET_ORDER_IGNORE = 0
PACKET_ORDER_WRONG = -1


def compare(left, right):
    """Compare 2 packets, return: RIGHT_ORDER, WRONG_ORDER or IGNORE"""
    if type(left) == int and type(right) == int:
        if left < right: return PACKET_ORDER_CORRECT
        if left == right: return PACKET_ORDER_IGNORE
        return PACKET_ORDER_WRONG

    if type(left) == list and type(right) == list:
        i = 0
        while i < len(left) and i < len(right):
            r = compare(left[i], right[i])
            if r != PACKET_ORDER_IGNORE: return r
            i += 1
        if i == len(left):
            if len(left) == len(right): return PACKET_ORDER_IGNORE
            return PACKET_ORDER_CORRECT # left packet was shorter
        return PACKET_ORDER_WRONG # right packet was shorter -> wrong order

    if type(left) == int and type(right) == list: return compare([left], right)
    else: return compare(left, [right])


with open("input") as data:
    pairs = [p.splitlines() for p in data.read().split("\n\n")]
    for i, p in enumerate(pairs):
        pairs[i][0] = eval(p[0])
        pairs[i][1] = eval(p[1])

answer = 0
for i, (left, right) in enumerate(pairs):
    if compare(left, right) == 1:
        answer += i + 1
print(f"{answer = }")
