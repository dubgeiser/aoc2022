#!/usr/bin/env python3

from monkeygames import *

monkeys = []
with open("input") as data:
    monkey_lines = data.read().split("\n\n")
    for ml in monkey_lines:
        mi = ml.split("\n")
        items = [int(i) for i in mi[1].strip().replace("Starting items: ", "").split(", ")]
        op = eval("lambda x: (x " + mi[2].replace("Operation: new = old ", "").replace("old", "x") + ") // 3")
        test = eval("lambda x: " + mi[4].split()[-1] + " if x % " + mi[3].split()[-1] + " == 0" + " else " + mi[5].split()[-1])
        monkeys.append(Monkey(items, op, test))


print()
play(monkeys, 20)
icounts = sorted([m.inspection_count for m in monkeys])
print(icounts[-1] * icounts[-2])
