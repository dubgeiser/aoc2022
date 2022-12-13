#!/usr/bin/env python3

from functools import cmp_to_key


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
    packets = list(map(eval, data.read().strip().replace("\n\n", "\n").split("\n")))
A = [[2]]
B = [[6]]
packets.append(A)
packets.append(B)
packets = sorted(packets, key=cmp_to_key(compare), reverse=True)
a = b = -1
for i, p in enumerate(packets):
    if p == A: a = i + 1
    if p == B: b = i + 1
print()
print(a*b)
