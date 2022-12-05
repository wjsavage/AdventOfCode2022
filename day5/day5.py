from typing import List
import itertools
import copy


def process_crate_input(crate_input: str) -> List[List[str]]:
    # transpose the crates except the bottom line - fill empty crate slots with '*'
    crate_lines = list(map(list, itertools.zip_longest(*crate_input.split('\n')[:-1], fillvalue='*')))
    # select only the lines with characters - these occur every 4 lines due to input spacing
    crate_lines = [crate_lines[i] for i in range(1, len(crate_lines), 4)]
    # filter out extra characters from lines to leave just crates and then reverse order
    crate_lines = [list(filter(lambda a: a not in ['*', ' '], crate))[::-1] for crate in crate_lines]

    return crate_lines


def process_inst_input(inst_input: str) -> List[List[int]]:
    insts = []
    for inst in inst_input.split('\n'):
        split = inst.split()
        insts.append([int(split[i]) - 1 for i in range(1, 6, 2)])
    return insts


def main() -> None:
    with open("input.txt") as file:
        crates, insts = file.read().split("\n\n")
    crates = process_crate_input(crates)
    insts = process_inst_input(insts)
    crates_b = copy.deepcopy(crates)

    for inst in insts:
        for _ in range(inst[0] + 1):
            crates[inst[2]].append(crates[inst[1]].pop())
    print(f"Part A: {''.join([x.pop() for x in crates])}")

    for inst in insts:
        crates_b[inst[2]].extend(
            [crates_b[inst[1]].pop() for _ in range(inst[0] + 1)][::-1]
        )

    print(f"Part B: {''.join([x.pop() for x in crates_b])}")


if __name__ == "__main__":
    main()
