# Advent of Code 2021 - Day 1 - Sonar Sweep
# https://adventofcode.com/2021/day/1

import sys
import functools

def parse_input(lines):
    return [int(line.strip()) for line in lines]

def part1(depths):
    total = 0
    for i in range(1,len(depths)):
        if depths[i] > depths[i-1]:
            total += 1
    return total

if __name__ == "__main__":
    print(part1(parse_input(sys.stdin.readlines())))

