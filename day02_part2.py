# Advent of Code 2021 - Day 2 - Dive! - Part 2
# https://adventofcode.com/2021/day/2

import sys
from day02_part1 import parse_input

def apply_moves(moves, position=0, depth=0, aim=0):
    for move in moves:
        if move[0] == 'forward':
            position += move[1]
            depth += aim * move[1]
        elif move[0] == 'down':
            aim += move[1]
        elif move[0] == 'up':
            aim -= move[1]
    return (position, depth)

def part2(moves):
    position, depth = apply_moves(moves)
    return position * depth

if __name__ == "__main__":
    print(part2(parse_input(sys.stdin.readlines())))

