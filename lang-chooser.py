#!/usr/bin/env python

import argparse
import logging
import random
from typing import List

logger = logging.getLogger(__name__)

def main() -> None:
    """The main entry point."""
    argparser = argparse.ArgumentParser()
    argparser.add_argument('--seed', help='Random seed value', type=int, default=3619117)
    argparser.add_argument('day', help='Day of challenge', type=int)
    args: argparse.Namespace = argparser.parse_args()

    random.seed(args.seed)

    languages = [
        'python',
        'perl',
        'ruby',
        'java',
        'scala',
        'c',
        'c++',
        'go',
        'rust',
        'javascript',
        'c#',
        'lua',
    ]

    for i in range(args.day):
        print(f'Print day {i+1} is {random.choice(languages)}')

if __name__ == "__main__":
    main()
