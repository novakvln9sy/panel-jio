#!/usr/bin/env python3
"""Tiny CLI that prints a random pick from a list."""
import argparse, random, sys

def pick(items):
    return random.choice(items)

def main(argv=None):
    ap = argparse.ArgumentParser(description="pick a random item")
    ap.add_argument("items", nargs="+")
    a = ap.parse_args(argv)
    print(pick(a.items))

if __name__ == "__main__":
    sys.exit(main())
