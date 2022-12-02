with open("input.txt") as file:
    plays = []
    for line in file.readlines():
        a, b = line.strip().split()
        plays.append((ord(a) - ord('A'), ord(b) - ord('X')))


def result_score(opponent, player):
    if (opponent - player + 3) % 3 == 1:
        return 0
    if opponent == player:
        return 3
    return 6


def calc_choice(opponent, result):
    if result == 0:
        return opponent if opponent > 0 else 3
    if result == 1:
        return opponent + 1
    return opponent + 2 if opponent < 2 else 1


print(f"Part A: {sum([result_score(opponent, player) + player + 1 for opponent, player in plays])}")
print(f"Part B: {sum([3 * result + calc_choice(opponent, result) for opponent, result in plays])}")