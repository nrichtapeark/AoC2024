#!/usr/bin/env python

import argparse
import logging
from dataclasses import dataclass
from typing import List,Tuple

logger = logging.getLogger(__name__)

@dataclass
class Point:
    x: int
    y: int

def search(lines: List[str], current_pos: Point, step: Point) -> bool:
    next_pos = Point(current_pos.x + step.x, current_pos.y + step.y)

    if next_pos.x < 0 or next_pos.y < 0:
        return False

    try:
        current_char: str = lines[current_pos.y][current_pos.x]
        next_char: str = lines[next_pos.y][next_pos.x]

        if current_char == 'X':
            if next_char == 'M':
                return search(lines, next_pos, step)
            return False
        
        if current_char == 'M':
            if next_char == 'A':
                return search(lines, next_pos, step)
            return False

        if current_char == 'A':
            return next_char == 'S'

        return False
    except IndexError:
        return False

def main() -> None:
    """The main entry point."""
    argparser = argparse.ArgumentParser()
    argparser.add_argument('-v', '--verbose', help='Verbose output', action='store_true', dest='verbose')
    argparser.add_argument('data', help='Name of data input file', type=str)
    args: argparse.Namespace = argparser.parse_args()

    if args.verbose:
        logging.basicConfig(level=logging.DEBUG, format='[%(process)d] (%(funcName)s) %(message)s')
    else:
        logging.basicConfig(level=logging.INFO, format='[%(process)d] (%(funcName)s) %(message)s')

    lines: List[str] = []
    with open(args.data, encoding='utf8') as data:
        for line in data:
            line = line.rstrip()
            lines.append(line)

    count: int = 0
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            c = lines[y][x]

            if c != 'X':
                continue

            if search(lines, Point(x, y), Point(1, 0)):
                count += 1
            if search(lines, Point(x, y), Point(-1, 0)):
                count += 1
            if search(lines, Point(x, y), Point(0, 1)):
                count += 1
            if search(lines, Point(x, y), Point(0, -1)):
                count += 1
            if search(lines, Point(x, y), Point(1, 1)):
                count += 1
            if search(lines, Point(x, y), Point(1, -1)):
                count += 1
            if search(lines, Point(x, y), Point(-1, 1)):
                count += 1
            if search(lines, Point(x, y), Point(-1, -1)):
                count += 1


    print(count)

if __name__ == "__main__":
    main()
