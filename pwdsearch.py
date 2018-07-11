#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Author: Nikita A. Medvedev <nikallass@yandex.ru>.

import os
import sys
if sys.version_info < (3, 0):
    sys.stdout.write("Sorry, this tool requires Python 3.x\n")
    sys.exit(1)
import re

import codecs

# Set accurace for Levenshtein distance. Less more accurate.
accuracy = 2


# Help message:
if len(sys.argv) == 2:
    help_message = \
'''Tool searching for different default passwords. It uses Levenshtein distance for fuzzy search. 

Usage:
    pwdsearch.py           ---    print all passwords in csv and GoGrepYourself.
    pwdsearch.py tp-link   ---    search for all passwords related to TP-Link devices (or similar word).

Hint: Use csvlook from csvkit to beautify csv in console.
    1) Install csvkit:
        sudo apt install csvkit
        or
        sudo pip install csvkit
    2) And then: 
        pwdsearch.py tp-link | csvlook
'''

    arg = sys.argv[1]
    if '-h' == arg or '--help' == arg:
        print(help_message)
        exit()

# Calculates the Levenshtein distance between a and b.
def distance(a, b):
    n, m = len(a), len(b)
    if n > m:
        # Make sure n <= m, to use O(min(n,m)) space
        a, b = b, a
        n, m = m, n

    if m-n > 3:
        return(100)

    current_column = range(n+1) # Keep current and previous column, not entire matrix
    for i in range(1, m+1):
        previous_column, current_column = current_column, [i]+[0]*n
        for j in range(1,n+1):
            add, delete, change = previous_column[j]+1, current_column[j-1]+1, previous_column[j-1]
            if a[j-1] != b[i-1]:
               change += 1
            current_column[j] = min(add, delete, change)

    return current_column[n]


# Get curr dir name:
dirname, filename = os.path.split(os.path.abspath(__file__))

# Main script:
res = []
with codecs.open(dirname + '/default-passwords.csv', "r",encoding='utf-8', errors='ignore') as f:
    header = f.readline().strip()
    body = f.read().encode("ascii", errors="ignore").decode().split('\r\n')
    
    if len(sys.argv) <= 1:
        print(header)
        for p in body: print(p)
        exit()

    find_term = sys.argv[1]
    find_term = find_term.lower()

    for line in body:
        for word in re.split(r';|,|\s|\*|"|\'|`|!|@|\$|%|\^|/|\.|\\\\|=|_| ', line):
            dist = distance(word.lower().replace('-', ''), find_term.replace('-', ''))
            if dist <= accuracy:
                res.append(str(dist) + '\t' + line)
                break


# Linux "head" tool bug fix. There was some problem while interrupting output (BrokenPipeError).
try:
    res = sorted(res)
    print(header)
    for l in res:
        print(l.split('\t')[1])
except (BrokenPipeError, IOError):
    pass    
