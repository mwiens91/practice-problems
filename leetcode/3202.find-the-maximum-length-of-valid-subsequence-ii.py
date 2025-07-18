# @leet start
class Solution:
    def maximumLength(self, nums: list[int], k: int) -> int:
        # A valid subsequence has alternating mod k values x and y,
        # where x is possibly equal to y. At each index i, we calculate
        # the longest subsequence we can make for each
        longest_subseq_lengths: dict[tuple[int, int], int] = {}

        for num in nums:
            current = num % k

            for prev in range(k):
                longest_subseq_lengths[(prev, current)] = (
                    longest_subseq_lengths.get((current, prev), 0) + 1
                )

        return max(longest_subseq_lengths.values())


# @leet end
