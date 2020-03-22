import sys
import argparse


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--city")
    parser.add_argument("-n", "--name")
    return parser


my_parser = create_parser()
arguments = my_parser.parse_args(sys.argv[1:])
print(f"Hello, {arguments.name}, I'm from {arguments.city}!")
