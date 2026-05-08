# @leet start
class Solution:
    def maxSumTwoNoOverlap(self, nums: list[int], firstLen: int, secondLen: int) -> int:
        n = len(nums)
        prefix_sums = [0] * (n + 1)

        for i in range(1, n + 1):
            prefix_sums[i] = prefix_sums[i - 1] + nums[i - 1]

        def helper(n_left: int, n_right: int) -> int:
            best_left = 0
            best = 0

            for i in range(n_left + n_right - 1, n):
                right = prefix_sums[i + 1] - prefix_sums[i + 1 - n_left]
                left = (
                    prefix_sums[i + 1 - n_left] - prefix_sums[i + 1 - n_left - n_right]
                )

                best_left = max(best_left, left)
                best = max(best, best_left + right)

            return best

        return max(helper(firstLen, secondLen), helper(secondLen, firstLen))


# @leet end
