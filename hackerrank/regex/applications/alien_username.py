#!/usr/bin/env python3

import re
import sys


# Read lines from stdin
lines = [line.strip() for line in sys.stdin.readlines()]

# Validate each name
for line in lines[1:]:
    if re.search(r'^[_.]\d+[a-zA-Z]*_?$', line):
        print('VALID')
    else:
        print('INVALID')
