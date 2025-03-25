# @leet start
class Solution:
    def maxPower(self, s: str) -> int:
        prev_char = None
        prev_count = 0

        max_count = 1

        for char in s:
            if char == prev_char:
                prev_count += 1
            else:
                max_count = max(max_count, prev_count)

                prev_char = char
                prev_count = 1

        return max_count


# @leet end
