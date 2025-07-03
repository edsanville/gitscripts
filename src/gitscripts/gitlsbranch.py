#!/usr/bin/env python3

import subprocess

from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import List


@dataclass
class GitBranch:
    name: str
    date: datetime


def getBranchList():
    results: List[GitBranch] = []

    # Get list of branch names
    branchNames = [n[2:] for n in subprocess.getoutput(f'git branch').split('\n')]

    # Get dates
    for branchName in branchNames:
        output = subprocess.getoutput(f"git log {branchName} --no-show-signature -1 --format=%cI")
        modifiedDate = datetime.fromisoformat(output)

        results.append(GitBranch(branchName, modifiedDate))

    return results


def timeDeltaToString(td: timedelta):

    periods = [
        ['year', 'years', timedelta(days=365)],
        ['month', 'months', timedelta(days=30)],
        ['week', 'weeks', timedelta(days=7)],
        ['day', 'days', timedelta(days=1)],
        ['hour', 'hours', timedelta(hours=1)],
        ['minute', 'minutes', timedelta(minutes=1)],
        ['second', 'seconds', timedelta(seconds=1)]
    ]

    for period in periods:
        periodTimedelta: timedelta = period[2]

        if td > periodTimedelta:
            count: float = td / periodTimedelta
            return f'{count:0.1f} {period[1]}'

    return '0 seconds'


def main():
    branches = getBranchList()
    branches.sort(key=lambda branch: branch.date, reverse=True)

    print('Git Branches')
    print(f'{"Age":20s}  {"Name":30s}')
    print()

    for branch in branches:
        age = datetime.now().astimezone() - branch.date
        ageString = timeDeltaToString(age)
        print(f'{ageString:20s}  {branch.name:30s}')


if __name__ == '__main__':
    main()
