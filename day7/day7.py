from typing import List
from dataclasses import dataclass


@dataclass
class Directory:
    name: str = None
    files: List = None
    child_directories: List['Directory'] = None
    parent_directory: 'Directory' = None
    size = 0


@dataclass
class File:
    name: str
    size: int


def check_if_dir_exists_if_not_make(current_dir: Directory, dir_name: str) -> Directory:
    poss_dir = None
    for directory in current_dir.child_directories:
        if directory.name == dir_name:
            poss_dir = directory
            break

    if poss_dir:
        nwd = poss_dir
    else:
        nwd = Directory(dir_name, [], [], current_dir)
        current_dir.child_directories.append(nwd)

    return nwd


def calculate_dir_size(root_dir: Directory, file_sizes: List[int]) -> None:
    root_dir.size = sum([x.size for x in root_dir.files]) + \
                    sum([calculate_dir_size(d, file_sizes) for d in root_dir.child_directories])
    file_sizes.append(root_dir.size)
    return root_dir.size


def main():
    with open("input.txt") as file:
        lines = [line.strip() for line in file.readlines()]

    home = Directory('/', [], [])
    cwd = home
    for line in lines[1:]:
        command = line.split(" ")
        if command[0] == '$' and command[1] == 'cd':
            if command[2] == '/':
                cwd = home
            elif command[2] == '..':
                cwd = cwd.parent_directory
            else:
                cwd = check_if_dir_exists_if_not_make(cwd, command[2])
        elif not command[0] == '$':
            if command[0] == 'dir':
                check_if_dir_exists_if_not_make(cwd, command[1])
            else:
                cwd.files.append(File(command[1], int(command[0])))

    file_sizes = []
    calculate_dir_size(home, file_sizes)
    small_dirs = filter(lambda x: x < 100000, file_sizes)
    print(f"Part A: {sum(small_dirs)}")

    size_available = 70000000 - home.size
    large_dirs = filter(lambda x: x > 30000000 - size_available, file_sizes)
    print(f"Part B: {min(large_dirs)}")


if __name__ == '__main__':
    main()
