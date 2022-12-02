# One line solution
with open("input.txt") as file:
    elves = sorted([sum(list(map(int, elf.split('\n')))) for elf in file.read().split("\n\n")], reverse=True)

# Part A
print(f"Part A Answer: {elves[1]}")

# Part B
print(f"Part B Answer: {sum(elves[:3])}")

# Space complexity of O(4), Tme complexity of O(n) where n is lines in input.txt
print()
with open("input.txt") as file:
    cur, top, mid, bottom = 0, 0, 0, 0
    for line in file.readlines():
        if len(line) > 1:
            cur += int(line.strip())
        else:
            if cur > top:
                top = cur
            elif cur > mid:
                mid = cur
            elif cur > bottom:
                bottom = cur
            cur = 0

# Part A
print(f"Part A Answer: {top}")

# Part B
print(f"Part B Answer: {sum([top, mid, bottom])}")


# Works with the ability to change n, with same time and space complexity
import heapq

top_n = 10
print()
print(f"We want to have the top {top_n} elves")
with open("input.txt") as file:
    cur = 0
    heap = []
    for line in file.readlines():
        if len(line) > 1:
            cur += int(line.strip())
        else:
            if len(heap) < top_n:
                heapq.heappush(heap, cur)
            else:
                heapq.heappushpop(heap, cur)
            cur = 0
# Part A
print(f"Part A Answer: {top}")

# Part B
print(f"Part B Answer: {sum(heap)}")
