import sys
import argparse
import Serhii_Hidenko.l_6_files.hw.task_1


CONDITIONS = (
    "all",
    "breakdowns",
    "without-breakdowns",
)


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--condition", required=True, choices=CONDITIONS)
    return parser


if __name__ == "__main__":

    my_parser = create_parser()
    arguments = my_parser.parse_args(sys.argv[1:])

    Serhii_Hidenko.l_6_files.hw.task_1.show_condition = arguments.condition

    Serhii_Hidenko.l_6_files.hw.task_1.main()
