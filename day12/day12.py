import heapq
from tqdm import tqdm


def get_valid_neigbours(pos, grid):
    x = pos[0]
    y = pos[1]
    xs = list(filter(lambda a: 0 <= a[0] <= len(grid[0]) - 1, [(x + dx, y) for dx in [-1, 1]]))
    ys = list(filter(lambda a: 0 <= a[1] <= len(grid) - 1, [(x, y + dy) for dy in [-1, 1]]))
    potential = xs + ys
    return list(filter(lambda p: is_valid_move(grid, pos, p), potential))


def is_valid_move(grid, pos, next_pos):
    return grid[next_pos[1]][next_pos[0]] - grid[pos[1]][pos[0]] < 2


def main() -> None:
    with open("input.txt") as file:
        lines = [line.strip() for line in file.readlines()]
    part_b = False

    topology_grid = []
    for line in lines:
        topology_grid.append([ord(x) - 97 for x in line.replace('S', 'a').replace('E', 'z')])

    starts, goal = [], (-1, -1)

    for j, line in enumerate(lines):
        for i, place in enumerate(line):
            if place == 'S':
                starts.append((i, j))
            if part_b and place == 'a':
                if any([topology_grid[pos[1]][pos[0]] == 1 for pos in get_valid_neigbours((i, j), topology_grid)]):
                    starts.append((i, j))
            elif place == 'E':
                goal = (i, j)

    ans = []
    for start in tqdm(starts):
        visited = set()
        visited.add(start)
        to_visit = []
        steps_to_reach = {start: 0}
        for neighbour in get_valid_neigbours(start, topology_grid):
            steps_to_reach[neighbour] = 1
            heapq.heappush(to_visit, (steps_to_reach[neighbour], neighbour))

        curr = start
        while to_visit:
            weight, new_curr = heapq.heappop(to_visit)
            curr = new_curr
            visited.add(curr)
            if curr == goal:
                break
            for neighbour in get_valid_neigbours(curr, topology_grid):
                if neighbour not in (list(visited) + [x[1] for x in to_visit]):
                    steps_to_reach[neighbour] = steps_to_reach[curr] + 1
                    heapq.heappush(to_visit, (steps_to_reach[neighbour], neighbour))

        ans.append(steps_to_reach[curr])
    print(f"Answer: {min(ans)}")


if __name__ == '__main__':
    main()
