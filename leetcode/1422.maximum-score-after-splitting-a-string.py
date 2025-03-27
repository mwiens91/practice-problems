# @leet start
class Solution:
    def maxScore(self, s: str) -> int:
        # Get the total number of 1s, assign them all to the right
        # substring initially
        right_ones = s.count("1")

        # Find the maximum count of zeros on the left substring and ones
        # on the right substring
        n = len(s)

        left_zeros = 0
        best_counts = 0

        for i in range(n - 1):
            if s[i] == "0":
                left_zeros += 1
            else:
                # s[i] == '1'
                right_ones -= 1

            best_counts = max(best_counts, left_zeros + right_ones)

        return best_counts


# @leet end
