# @leet start
class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        n = len(s)
        i = 0

        longest = 0

        while i < n:
            zeros_count = 0

            while i < n and s[i] == "0":
                zeros_count += 1
                i += 1

            ones_count = 0

            while i < n and s[i] == "1":
                ones_count += 1
                i += 1

            longest = max(longest, 2 * min(zeros_count, ones_count))

        return longest


# @leet end
