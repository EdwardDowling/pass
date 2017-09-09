#!/usr/bin/env python

import sys
import hashlib
import dmenu
import clipboard

LINE_NUMBER = 10

def hash(string):
    return hashlib.sha224(string.encode('utf-8')).hexdigest()

def select(options):
    return dmenu.show(options, lines=LINE_NUMBER, case_insensitive=True)

def load_salt(location):
    with open(location) as f:
        return [s.strip() for s in f.readlines()]

def get_password():
    password = dmenu.show([], foreground='#feca1e', background='#feca1e')
    if not password:
        sys.exit()    
    return password
 
if __name__ == '__main__':
    clipboard.copy(hash(get_password() + select(load_salt(sys.argv[1]))))
