#!/usr/bin/env python3

import argparse

import rpc_client


def deploy(src: str, dst: str, *filenames: str):
    client = rpc_client.Client()
    return client.call("deploy", src, dst, filenames)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("src")
    parser.add_argument("dst")
    parser.add_argument("filenames", nargs="*")
    args = parser.parse_args()

    print(deploy(args.src, args.dst, *args.filenames))


if __name__ == "__main__":
    main()
