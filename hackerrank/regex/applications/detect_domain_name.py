#!/usr/bin/env python3

import re
import sys


# Read lines from stdin
lines = [line.strip() for line in sys.stdin.readlines()]

# Pattern to match a domain
domain_pattern = r'\bhttps?://(?:www\.)?([-a-zA-Z0-9.]+\.[a-z]+)(?:/[-a-zA-Z0-9.]*)*\b'

# Now match all the domains in the input
domains = []

for line in lines[1:]:
    domains += re.findall(domain_pattern, line)

# Print the domains
print(';'.join(sorted(list(set(domains)))))
