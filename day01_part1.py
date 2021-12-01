# Advent of Code 2021 - Day 1 - Sonar Sweep
# https://adventofcode.com/2021/day/1

import sys

def parse_input(lines):
    return [int(line.strip()) for line in lines]

def total_increases(depths, window_size=1):
    return sum(a < b for a,b in zip(depths, depths[window_size:]))

def part1(depths):
    return total_increases(depths)

if __name__ == "__main__":
    print(part1(parse_input(sys.stdin.readlines())))

