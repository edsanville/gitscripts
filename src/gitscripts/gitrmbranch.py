#!/usr/bin/env python3

import sys
import os

def main():
    branch_name = sys.argv[1]

    os.system(f'git push -d origin {branch_name}')
    os.system(f'git branch -d {branch_name}')


if __name__ == '__main__':
    main()
