from collections import defaultdict
import math
import heapq
from functools import reduce
from operator import mul
from dataclasses import dataclass

@dataclass
class MonkeyData:
    equation: str
    divisor: int
    true_dest: int
    false_dest: int


def main() -> None:
    with open("input.txt") as file:
        monkeys = [line for line in file.read().split('\n\n')]

    monkey_inspect_count = defaultdict(int)
    monkey_items = {}
    monkey_data = []

    LCM = 1
    for i, monkey in enumerate(monkeys):
        lines = [line.strip() for line in monkey.split('\n')][1:]
        monkey_items[i] = list(map(int, lines[0].split(':')[1].strip().split(',')))

        equation = lines[1].split('=')[1].strip()
        divisor, true_dest, false_dest = [int(lines[x].split(" ")[-1]) for x in [2,3,4]]
        LCM *= divisor
        monkey_data.append(MonkeyData(equation, divisor, true_dest, false_dest))

    for round in range(10_000):
        for i, monkey in enumerate(monkeys):
            monkey_inspect_count[i] += len(monkey_items[i])
            data = monkey_data[i]

            monkey_items[i] = [eval(data.equation) for old in monkey_items[i]]
            # monkey_items[i] = [int(math.floor(item/3)) for item in monkey_items[i]]
            monkey_items[i] = [item % LCM for item in monkey_items[i]]

            for val in monkey_items[i]:
                if not val % data.divisor:
                    monkey_items[data.true_dest].append(val)
                else:
                    monkey_items[data.false_dest].append(val)
            monkey_items[i] = []

    print(f"Answer: {reduce(mul, sorted(monkey_inspect_count.values())[-2:], 1)}")


if __name__ == '__main__':
    main()
