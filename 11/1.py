#!/usr/bin/env python3

class Monkey:
    def __init__(self, items, operation, test) -> None:
        self.items = items
        self.operation = operation
        self.test = test
        self.inspection_count = 0

    def update(self, monkeys: list["Monkey"]):
        items = self.items.copy()
        items.reverse()
        while len(items) > 0:
            i = items.pop()
            i = self.operation(i)
            self.inspection_count += 1
            target_monkey = self.test(i)
            monkeys[target_monkey].receive(i)
        self.items = []

    def receive(self, i: int):
        self.items.append(i)



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
ROUNDS =  20
for _ in range(ROUNDS):
    for m in monkeys:
        m.update(monkeys)

icounts = sorted([m.inspection_count for m in monkeys])
print(icounts[-1] * icounts[-2])
