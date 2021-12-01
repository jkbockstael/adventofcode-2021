# Advent of Code 2021 - Day 1 - Sonar Sweep - Part 2
# https://adventofcode.com/2021/day/1

import sys
from day01_part1 import parse_input, total_increases

def part2(depths):
    return total_increases(depths, 3)

if __name__ == "__main__":
    print(part2(parse_input(sys.stdin.readlines())))

