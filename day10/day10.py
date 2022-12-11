def main() -> None:
    with open("input.txt") as file:
        lines = [line.strip() for line in file.readlines()]

    # (cycle_start, val)
    cycle_states = [(1, 1)]
    for line in lines:
        command = line.split(" ")
        curr = cycle_states[-1]
        cycle_states.append((curr[0] + 1, curr[1]))
        if command[0] == "addx":
            cycle_states.append((curr[0] + 2, curr[1] + int(command[1])))

    cycle_dict = {x: y for (x, y) in cycle_states}
    print(sum([cycle_dict[i] * i for i in range(20, 221, 40)]))

    CRT = []
    for i, state in enumerate(cycle_states):
        pixel_pos = i % 40
        if abs(pixel_pos - state[1]) < 2:
            CRT.append('#')
        else:
            CRT.append('.')

    for i, j in zip(range(0, 201, 40), range(40, 241, 40)):
        print("".join(CRT[i: j]))


if __name__ == '__main__':
    main()
