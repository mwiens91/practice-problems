#!/usr/bin/env python3

import re
import sys


# Read lines from stdin
lines = [line.strip() for line in sys.stdin.readlines()]

# Regex patterns for IP address types
ipv4_chunk = r'((25[0-5])|(2[0-4]\d)|([01]?\d?\d))'
ipv4_pattern = ipv4_chunk + r'(\.' + ipv4_chunk + r'){3}$'
ipv6_chunk = r'([0-9a-f]{1,4})'
ipv6_pattern = ipv6_chunk + r'(:' + ipv6_chunk + r'){7}$'

# Go through each IP address candidate line
for line in lines[1:]:
    if re.match(ipv4_pattern, line):
        print("IPv4")
    elif re.match(ipv6_pattern, line):
        print("IPv6")
    else:
        print("Neither")
