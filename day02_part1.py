# Advent of Code 2021 - Day 2 - Dive!
# https://adventofcode.com/2021/day/2

import sys

def parse_input(lines):
    tokens = [line.split(' ') for line in lines]
    return [(token[0], int(token[1])) for token in tokens]

def apply_moves(moves, position=0, depth=0):
    for move in moves:
        if move[0] == 'forward':
            position += move[1]
        elif move[0] == 'down':
            depth += move[1]
        elif move[0] == 'up':
            depth -= move[1]
    return (position, depth)

def part1(moves):
    position, depth = apply_moves(moves)
    return position * depth

if __name__ == "__main__":
    print(part1(parse_input(sys.stdin.readlines())))

