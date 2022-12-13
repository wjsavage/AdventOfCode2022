import json
from functools import cmp_to_key


def convert_first_val_to_list(input):
    if not input:
        return []
    if len(input) == 1:
        return [input]
    return [[input[0]], input[1:]]


def is_less_than(first, second):
    if not first and not second:
        return None
    if not first and second:
        return True
    if first and not second:
        return False

    if isinstance(first[0], int) and isinstance(second[0], int):
        if first[0] == second[0]:
            return is_less_than(first[1:], second[1:])
        return first[0] < second[0]

    if isinstance(first[0], int) and isinstance(second[0], list):
        return is_less_than(convert_first_val_to_list(first), second)
    if isinstance(first[0], list) and isinstance(second[0], int):
        return is_less_than(first, convert_first_val_to_list(second))

    if isinstance(first[0], list) and isinstance(second[0], list):
        test = is_less_than(first[0], second[0])
        if test is not None:
            return test
        return is_less_than(first[1:], second[1:])


def make_comparator(less_than):
    def compare(x, y):
        if less_than(x, y):
            return -1
        elif less_than(y, x):
            return 1
        else:
            return 0
    return compare


def main() -> None:
    with open("input.txt") as file:
        pairs = [list(map(json.loads, x.split('\n'))) for x in file.read().split("\n\n")]

    total = 0
    for i, pair in enumerate(pairs, 1):
        if is_less_than(pair[0], pair[1]):
            total += i
    print(f"Part A: {total}")

    all_items = [item for sublist in pairs for item in sublist]
    two, six = [[2]], [[6]]
    all_items.extend([two, six])
    all_items.sort(key=cmp_to_key(make_comparator(is_less_than)))
    n, m = all_items.index(two) + 1, all_items.index(six) + 1
    print(f"Part B: {n * m}")


if __name__ == '__main__':
    main()
