from copy import deepcopy

def calc_tail_head_distance(head, tail):
    if head[0] == tail[0] and head[1] == tail[1]:
        return 0
    if head[0] == tail[0]:
        return abs(head[1] - tail[1])
    if head[1] == tail[1]:
        return abs(head[0] - tail[0])
    if abs(head[0] - tail[0]) == 1 and abs(head[1] - tail[1]) == 1:
        return 1
    # it's not next to the head so must be at least 2 steps
    return 2


def move_tail(head, tail, old_head):
    distance = calc_tail_head_distance(head, tail)
    if distance < 2:
        return tail
    else:
        return old_head


def main() -> None:
    with open("input.txt") as file:
        lines = [line.strip() for line in file.readlines()]
    print(lines)

    # (x, y)
    head_pos = [0, 0]
    tail_pos = [0, 0]
    visited_states = set()
    visited_states.add(tuple(tail_pos))
    print(visited_states)
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
            tail_pos = move_tail(head_pos, tail_pos, old_head)
            visited_states.add(tuple(tail_pos))
    print(len(visited_states))


if __name__ == '__main__':
    main()
