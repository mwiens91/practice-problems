# @leet start
class Solution:
    def minSwaps(self, s: str) -> int:
        count = 0

        left = 0
        right = len(s) - 1
        left_opened = 0
        right_closed = 0

        while left < right:
            if s[left] == "[" or left_opened:
                left_opened += 1 if s[left] == "[" else -1
                left += 1
            elif s[right] == "]" or right_closed:
                right_closed += 1 if s[right] == "]" else -1
                right -= 1
            else:
                count += 1
                left += 1
                right -= 1
                left_opened += 1
                right_closed += 1

        return count


# @leet end
