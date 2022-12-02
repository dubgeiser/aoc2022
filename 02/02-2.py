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
rock = 1
paper = 2
scissors = 3

# A -> Rock, B -> Paper, C -> scissors
# X -> lose, Y -> draw, Z -> win
outcomes = {
        ('A', 'X') : loss + scissors, 
        ('A', 'Y') : draw + rock,
        ('A', 'Z') : win + paper,
        ('B', 'X') : loss + rock,
        ('B', 'Y') : draw + paper,
        ('B', 'Z') : win + scissors,
        ('C', 'X') : loss + paper,
        ('C', 'Y') : draw + scissors,
        ('C', 'Z') : win + rock,
        }


def solve(data):
    score = 0
    for each in data:
        score += outcomes[each]
    return score


if __name__ == "__main__":
    answer = solve(read_data_file("input"))
    print(f"{answer = }")
