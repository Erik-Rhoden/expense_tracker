#!/usr/bin/env python3

from src.cli import setup_parser

def main():
    parser = setup_parser()
    args = parser.parse_args()

    print(vars(args))

if __name__ == "__main__":
    main()
