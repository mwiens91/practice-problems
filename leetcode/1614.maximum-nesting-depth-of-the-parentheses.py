# @leet start
class Solution:
    def maxDepth(self, s: str) -> int:
        # Keep track of the current depth, which is a count of the
        # number of opening brackets minus the number of closing
        # brackets we've encountered. When we reach a closing bracket,
        # update the maximum depth using the current depth (if it's
        # larger) and then decrement the current depth.
        OPENING_BRACKET = "("
        CLOSING_BRACKET = ")"

        current_depth = 0
        max_depth = 0

        for char in s:
            if char == OPENING_BRACKET:
                current_depth += 1
            elif char == CLOSING_BRACKET:
                max_depth = max(max_depth, current_depth)

                current_depth -= 1

        return max_depth


# @leet end
