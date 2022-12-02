#!/usr/bin/env python3


def read_data_file(fn):
    scores = []
    with open(fn) as data:
        for line in data:
            score_elf, score_me = line.strip().split(' ')
            scores.append((score_elf, score_me))
    return scores


loss = 0
draw = 3
win = 6
outcomes = {
        ('A', 'X') : draw, 
        ('A', 'Y') : win,
        ('A', 'Z') : loss,
        ('B', 'X') : loss,
        ('B', 'Y') : draw,
        ('B', 'Z') : win,
        ('C', 'X') : win,
        ('C', 'Y') : loss,
        ('C', 'Z') : draw,
        }
scoremap = {
        'X' : 1, # Rock
        'Y' : 2, # Paper
        'Z' : 3, # Scissors
        }
def solve(data):
    score = 0
    for each in data:
        score += outcomes[each] + scoremap[each[1]]
    return score


if __name__ == "__main__":
    answer = solve(read_data_file("input"))
    print(f"{answer = }")
