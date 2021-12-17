#!/usr/bin/env python3

import argparse


def deploy(src: str, dst: str):
    print(f"deploy({src}, {dst})")  # TODO


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("src")
    parser.add_argument("dst")
    args = parser.parse_args()

    deploy(args.src, args.dst)


if __name__ == "__main__":
    main()
