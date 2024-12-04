#!/usr/bin/env python

import argparse
import logging
from dataclasses import dataclass
from typing import List,Optional

logger = logging.getLogger(__name__)

@dataclass
class Point:
    x: int
    y: int

def find_char(lines: List[str], pos: Point, step: Point) -> str:
    next_pos = Point(pos.x + step.x, pos.y + step.y)

    if next_pos.x < 0 or next_pos.y < 0:
        return 'A'

    try:
        char: str = lines[next_pos.y][next_pos.x]

        return char
    except IndexError:
        return 'A'

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

            if c != 'A':
                continue

            left_up = find_char(lines, Point(x, y), Point(-1, -1))
            left_down = find_char(lines, Point(x, y), Point(-1, 1))
            right_up = find_char(lines, Point(x, y), Point(1, -1))
            right_down = find_char(lines, Point(x, y), Point(1, 1))

            if left_up not in ['M', 'S']:
                continue

            if left_down not in ['M', 'S']:
                continue

            if right_up not in ['M', 'S']:
                continue

            if right_down not in ['M', 'S']:
                continue

            if left_up == 'M' and right_down != 'S':
                continue

            if left_up == 'S' and right_down != 'M':
                continue

            if left_down == 'M' and right_up != 'S':
                continue

            if left_down == 'S' and right_up != 'M':
                continue

            count += 1

    print(count)

if __name__ == "__main__":
    main()
