with open("test_input.txt") as file:
    plays = []
    for line in file.readlines():
        a, b = line.strip().split()
        plays.append((ord(a) - ord('A'), ord(b) - ord('X')))
#
print(plays)


def part_a():
    print(sum([b+1 + (((b+1 - a) % 3) * 3) for a, b in plays]))


def part_b():
    print(sum([b*3 + (((a+b+2) % 3) + 1) for a, b in plays]))


part_a()
part_b()
