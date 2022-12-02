with open("input.txt") as file:
    lines = [line.rstrip().split(" ") for line in file.readlines()]

result_score = {
    'X': 0, # Rock
    'Y': 3, # Paper
    'Z': 6 # Scissors
}

choice_score = {
    'A': 1, # Rock
    'B': 2, # Paper
    'C': 3 # Scissors
}





print(total_score)