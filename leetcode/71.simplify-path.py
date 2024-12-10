# @leet start
import re


class Solution:
    def simplifyPath(self, path: str) -> str:
        # Truncate any repeated slashes
        path = re.sub(r"/+", r"/", path)

        # Remove trailing slash
        path = re.sub(r"/$", "", path)

        # Deal with current and previous working directories ('.'s and
        # '..'s)
        path_parts = path.split("/")

        # We'll store what parts to keep here and merge them later
        parts_to_keep_stack = []

        CURR_WD = "."
        PREV_WD = ".."

        for part in path_parts:
            if part == PREV_WD:
                # We want to keep an empty string generated from the
                # starting "/" in here, which is why we only pop when
                # length is 2 or more
                if len(parts_to_keep_stack) > 1:
                    parts_to_keep_stack.pop()
            elif part != CURR_WD:
                parts_to_keep_stack.append(part)

        # For edge cases where we only keep an empty string, we need to
        # have the below conditional
        return "/".join(parts_to_keep_stack) if len(parts_to_keep_stack) > 1 else "/"


# @leet end
