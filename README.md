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


## Day 15
This is the day that kinda got me; part 1 took a couple of hours, then I let go of AoC for a couple of days, 'cause my heart and head weren't in it.
Revisiting part 1 and catching the inefficient way of determining the positions that cannot contain a beacon and that we're dealing with intervals here, gave me back my motivation to optimize it so that I could finally finish part 2.
Still part 2 is very inefficient and when timing and motivation permits I should revisit it, there's got to be a much more efficient way to determine the position of the distress signal.
