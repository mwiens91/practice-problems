# @leet start
class Solution:
    def maxCount(self, banned: list[int], n: int, maxSum: int) -> int:
        # Greedily take as many numbers as possible that aren't banned
        # until we cannot add more.
        banned_set = set(banned)

        current_sum = 0
        count = 0

        for x in range(1, n + 1):
            if x + current_sum > maxSum:
                # We can't add any more numbers
                break
            elif x not in banned_set:
                # Add the current number
                current_sum += x
                count += 1

        return 1


# @leet end
