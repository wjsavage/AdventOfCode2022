from copy import deepcopy
import math
import sys
import numpy as np
np.set_printoptions(threshold=sys.maxsize)
np.set_printoptions(linewidth=np.inf)


def plot_grid(head, tails):
    size = 30
    half = int(size/2)
    grid = np.zeros((size, size))
    grid[half, half] = -2
    for i, t in enumerate(tails[::-1], 0):
        grid[half + t[1], half + t[0]] = 9-i

    grid[half + head[1], half + head[0]] = -1
    print(grid)


def calc_tail_head_distance(head, tail):
    return math.sqrt(abs(head[0] - tail[0])**2 + abs(head[1] - tail[1])**2)


def move_tail(head, tail, old_head):
    distance = calc_tail_head_distance(head, tail)

    if distance <= math.sqrt(2):
        return tail

    new_tail = deepcopy(tail)
    if head[0] < tail[0]:
        new_tail[0] -= 1
    elif head[0] > tail[0]:
        new_tail[0] += 1
    if head[1] < tail[1]:
        new_tail[1] -= 1
    elif head[1] > tail[1]:
        new_tail[1] += 1

    return new_tail


def main() -> None:
    with open("input.txt") as file:
        lines = [line.strip() for line in file.readlines()]

    # (x, y)
    head_pos = [0, 0]
    tails = [[0, 0]] * 9
    old_tails = deepcopy(tails)
    visited_states = set()
    visited_states.add(tuple(tails[8]))

    plot_grid(head_pos, tails)

    for line in lines:
        direction, steps = line.split(" ")
        for turn in range(int(steps)):
            old_head = deepcopy(head_pos)
            if direction == 'L':
                head_pos[0] -= 1
            elif direction == 'R':
                head_pos[0] += 1
            elif direction == 'U':
                head_pos[1] -= 1
            elif direction == 'D':
                head_pos[1] += 1
            old_tails[0] = deepcopy(tails[0])
            tails[0] = move_tail(head_pos, tails[0], old_head)

            for i, tail in enumerate(tails[1:], 1):
                old_tails[i] = deepcopy(tail)
                tails[i] = move_tail(tails[i-1], tail, old_tails[i-1])

            visited_states.add(tuple(tails[8]))

        # plot_grid(head_pos, tails)
    print(len(visited_states))


if __name__ == '__main__':
    main()
