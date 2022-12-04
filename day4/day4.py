with open("input.txt") as file:
    lines = [line.rstrip() for line in file.readlines()]

total_A, total_B = 0, 0
for line in lines:
    ends_A, ends_B = sorted([list(map(int, x.split('-'))) for x in line.split(',')],
                            key=lambda x: x[0])

    if ends_B[1] <= ends_A[1]:
        total_A += 1

    if ends_B[0] <= ends_A[1]:
        total_B += 1

print(f"Part A: {total_A}")
print(f"Part B: {total_B}")
