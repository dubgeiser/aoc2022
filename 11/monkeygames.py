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


def play(monkeys: list[Monkey], rounds: int):
    for _ in range(rounds):
        for m in monkeys:
            m.update(monkeys)
