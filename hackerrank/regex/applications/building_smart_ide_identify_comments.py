#!/usr/bin/env python3

import re
import sys


# Read lines from stdin
lines = sys.stdin.readlines()

# Stitch together the input lines
joined_lines = ''.join(lines)

# Pattern to match comments
single_comment_pattern = r'(?:(//.*?)$)'
multiline_comment_pattern = r'(/\*(?:.|\n)*?\*/)'
full_comment_pattern = (single_comment_pattern
                        + r'|'
                        + multiline_comment_pattern)

# Now match all the comment lines in the input
comment_lines_raw = re.findall(full_comment_pattern,
                               joined_lines,
                               flags=re.MULTILINE)

# Clean up the output of the above regex function
comment_lines = []

for matchpair in comment_lines_raw:
    for match in matchpair:
        # Remove empty strings
        if match:
            # Split at a '\n'
            comments = match.splitlines()

            # Strip leading and trailing whitespace on each line
            for comment in comments:
                comment_lines += [comment.strip()]

# Print the comments
print('\n'.join(comment_lines))
