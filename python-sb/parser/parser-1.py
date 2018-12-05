#!/usr/bin/env python
import argparse

if __name__ == '__main__':
    # Initialize the parser
    parser = argparse.ArgumentParser(
        description="simple script to demonstrate argparse usage"
    )

    # Add the positional parameter
    parser.add_argument('printme', help="The string to be printed")

    # Parse the arguments
    arguments = parser.parse_args()

    # Finally print the passed string
    print(arguments.printme)

parser.add_argument(
    '-r', '--repeat',
    help="number of times to print the string",
    type=int,
    default=1
)

for i in range(0, arguments.repeat):
    print(arguments.printme)


