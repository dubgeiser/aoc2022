#!/usr/bin/env python3

from collections import defaultdict

sample = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""


print()
with open("input") as data:
    commands = [l.strip() for l in data]

total_diskspace = 70000000
min_available_space = 30000000

answer = 0
dirsizes = defaultdict(int)
curdir = []
for c in commands:
    if c == "$ cd ..":
        curdir.pop()
    elif c == "$ cd /":
        curdir = ["/"]
    elif c.startswith("$ cd"):
        curdir.append(c.replace("$ cd ", ""))
    elif c == "$ ls":
        continue
    elif c.startswith("dir"):
        continue
    else: # can be but a file.
        size, fn = c.split(" ")
        dir = curdir.copy()
        while len(dir) > 0:
            dirsizes["/".join(dir)] += int(size)
            dir.pop()

def delete_smallest_possible_dir():
    total_dir_size = dirsizes["/"]
    while len(dirsizes.items()) > 1:
        dir, size = min(dirsizes.items(), key=lambda x: x[1])
        if total_diskspace - total_dir_size + size >= min_available_space:
            return size
        else:
            dirsizes.pop(dir)

answer = delete_smallest_possible_dir()

print(f"{answer = }")
