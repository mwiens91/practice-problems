#!/usr/bin/env python3

import re
import sys


# Read lines from stdin
lines = [line.strip() for line in sys.stdin.readlines()]

# Join all lines together for convenience. Assume emails aren't split
# across multiple lines.
textblock = ' '.join(lines[1:])

# Find all the email addresses - match *basic* email addresses. I'm not
# going overboard here with matching corner cases.
emails = re.findall(r'[a-zA-Z0-9._]+@[a-zA-Z0-9.]+\.[a-z]+', textblock)

# Print the email addresses
print(';'.join(sorted(list(set(emails)))))
