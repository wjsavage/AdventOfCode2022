import numpy as np
from functools import reduce
from typing import List


def generate_views(i: int, j: int, grid: List[List[int]]) -> List[List[int]]:
    left = [grid[j][a] for a in range(0, i)][::-1]
    right = [grid[j][a] for a in range(i + 1, len(grid[j]))]
    up = [grid[b][i] for b in range(0, j)][::-1]
    down = [grid[b][i] for b in range(j + 1, len(grid))]
    return [left, right, up, down]


def calc_visible_distance(height: int, line: List[int]) -> int:
    for i, tree in enumerate(line):
        if tree >= height:
            return i + 1
    return len(line)


def calc_tree_score(tree_height: int, views: List[List[int]]) -> int:
    return reduce((lambda x, y: x * y), [
        calc_visible_distance(tree_height, views[x]) for x in range(4)
    ])


def is_visible(tree: int, views: List[List[int]]) -> bool:
    if not any([val >= tree for val in views[0]]):
        return True
    if not any([val >= tree for val in views[1]]):
        return True
    if not any([val >= tree for val in views[2]]):
        return True
    if not any([val >= tree for val in views[3]]):
        return True


def main() -> None:
    with open("input.txt") as file:
        tree_grid = [list(map(int, list(line.strip()))) for line in file.readlines()]

    visible_grid = np.full((len(tree_grid), len(tree_grid[0])), True, dtype=bool)
    visible_grid[1: -1, 1: -1] = False
    sight_grid = np.full((len(tree_grid), len(tree_grid[0])), 0, dtype=int)

    for j in range(1, len(visible_grid) - 1):
        for i in range(1, len(visible_grid[0]) - 1):
            tree_height = tree_grid[j][i]
            views = generate_views(i, j, tree_grid)

            visible_grid[i, j] = is_visible(tree_height, views)
            sight_grid[i, j] = calc_tree_score(tree_height, views)

    print(f"Part A: {visible_grid.sum()}")
    print(f"Part B: {sight_grid.max(initial=0)}")


if __name__ == "__main__":
    main()
