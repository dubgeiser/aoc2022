# Advent Of Code 2022
My solutions for Advent Of Code 2022

Code is up for grabs, public domain.

Every day is a directory with 2 scripts for each part and the input file.

Puzzles should normally be found on https://adventofcode.com/2022/


## Day 13
Gotcha!
This:
```python
if type(left) == list and type(right) == list:
    if len(left) == len(right):
        for i in range(len(left)):
            r = compare(left[i], right[i])
            if r != 0: return r
        return 0
    if len(left) < len(right): return 1
    else: return -1
```
did not work and resulted in too many counts (sample worked)
Needed to exhaust the lists and compare them first!
