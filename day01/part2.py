#!/usr/bin/env python

import argparse
import logging
import random
from typing import List

logger = logging.getLogger(__name__)

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


    left: List[int] = []
    right: List[int] = []

    with open(args.data, encoding='utf8') as data:
        for line in data:
            line = line.rstrip()

            a, b = line.split()
        
            left.append(int(a))
            right.append(int(b))

    score: int = 0
    for i,a in enumerate(left):
        score += a * right.count(a)

    print(score)

if __name__ == "__main__":
    main()
