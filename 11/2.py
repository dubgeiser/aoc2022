#!/usr/bin/env python3

from monkeygames import *


monkeys = []
mod_divider = 1
with open("input") as data:
    monkey_lines = data.read().split("\n\n")
    for ml in monkey_lines:
        mi = ml.split("\n")
        items = [int(i) for i in mi[1].strip().replace("Starting items: ", "").split(", ")]
        op = "lambda x: (x " + mi[2].replace("Operation: new = old ", "").replace("old", "x") + ") % @@@@@"
        divisible_by = mi[3].split()[-1]
        test = eval("lambda x: " + mi[4].split()[-1] + " if x % " + divisible_by + " == 0" + " else " + mi[5].split()[-1])
        monkeys.append(Monkey(items, op, test))
        mod_divider *= int(divisible_by)
for m in monkeys: m.operation = eval(m.operation.replace("@@@@@", str(mod_divider)))
print()
play(monkeys, 10_000)
icounts = sorted([m.inspection_count for m in monkeys])
print(icounts[-1] * icounts[-2])
