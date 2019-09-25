# ** coding = utf8 **
import sys
import os
import argparse
from getpass import getuser
from lib.Runner import machine_test

def user_parser():
    parser = argparse.ArgumentParser(description='just an example.')
    parser.add_argument('name', nargs='?', default=getuser(), help='The name of someone to greet')
    parser.add_argument('--verbose', '-v', action='count')

    args = parser.parse_args()
    if not args.verbose:
        print('Try running this again with multiple "-v" flags!')
        exit(0)
    greeting = ['Hi', 'Hello', 'Greetings! its very nice to meet you'][args.verbose % 3]
    print(f'{greeting}, {args.name}')

if __name__ == '__main__':
    machine_test()