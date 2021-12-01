# Advent of Code 2021 - Day 1 - Sonar Sweep - Part 2
# https://adventofcode.com/2021/day/1

import sys
import functools
from day01_part1 import parse_input, part1

def part2(depths):
    sums = []
    for i in range(2,len(depths)):
        sums.append(depths[i] + depths[i-1] + depths[i-2])
    return sums

if __name__ == "__main__":
    print(part1(part2(parse_input(sys.stdin.readlines()))))

