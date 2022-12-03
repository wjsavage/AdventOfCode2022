import string

with open("input.txt") as file:
    lines = [line.rstrip() for line in file.readlines()]

total = 0
for line in lines:
    mid = int(len(line) / 2)
    common = list(set(line[:mid]) & set(line[mid:]))[0]
    total += string.ascii_letters.index(common) + 1

print(f"Part A: {total}")

from itertools import zip_longest

total = 0
for a, b, c in zip_longest(*([iter(lines)] * 3), fillvalue=None):
    common = list(set(a) & set(b) & set(c))[0]
    total += string.ascii_letters.index(common) + 1

print(f"Part B: {total}")
