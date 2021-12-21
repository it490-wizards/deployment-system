#!/usr/bin/env python3

import argparse
import os.path

import rpc_client


def deploy(src: str, dst: str, add: list, rm: list):
    client = rpc_client.Client()
    return client.call(
        "deploy",
        src,
        dst,
        [os.path.abspath(f) for f in add],
        [os.path.abspath(f) for f in rm],
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("src", help="IP address of source host")
    parser.add_argument("dst", help="IP address of destination host")
    parser.add_argument("--add", nargs="*", help="list of paths to add", default=[])
    parser.add_argument("--rm", nargs="*", help="list of paths to remove", default=[])
    args = parser.parse_args()

    print(deploy(args.src, args.dst, args.add, args.rm))


if __name__ == "__main__":
    main()
