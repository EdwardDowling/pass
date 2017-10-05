#!/usr/bin/env python

import clipboard
import dmenu
import hashlib
import sys


MAX_LINES = 10


def hash(string):
    return hashlib.sha224(string.encode('utf-8')).hexdigest()


def select(options):
    return dmenu.show(options, lines=MAX_LINES, case_insensitive=True)


def load_salt(location):
    with open(location) as file:
        return [line.strip() for lines in file.readlines()]


def get_password():
    password = dmenu.show([], foreground='#feca1e', background='#feca1e')
    if not password:
        sys.exit(1)
    return password


if __name__ == '__main__':
    clipboard.copy(hash(get_password() + select(load_salt(sys.argv[1]))))
