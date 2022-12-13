def first_first_unique_n(input: str, n: int) -> int:
    for i in range(n, len(input) + 1):
        if len(set(input[i-n: i])) == len(input[i-n: i]):
            return i


def main() -> None:
    with open("input.txt") as file:
        input = [x.strip() for x in file.readlines()][0]

    print(f"Part A: {first_first_unique_n(input, 4)}")
    print(f"Part B: {first_first_unique_n(input, 14)}")


if __name__ == "__main__":
    main()
