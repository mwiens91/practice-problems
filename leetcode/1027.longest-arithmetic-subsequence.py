# @leet start
class Solution:
    def longestArithSeqLength(self, nums: list[int]) -> int:
        # Store for each index i, the longest sequence with a given
        # difference
        max_lengths_at_idx: list[dict[int, int]] = [{} for _ in range(len(nums))]
        max_seq_length = 1

        for current_idx, num in enumerate(nums):
            for prev_idx in range(current_idx):
                diff = num - nums[prev_idx]

                max_lengths_at_idx[current_idx][diff] = (
                    max_lengths_at_idx[prev_idx].get(diff, 1) + 1
                )

                max_seq_length = max(
                    max_seq_length, max_lengths_at_idx[current_idx][diff]
                )

        return max_seq_length


# @leet end
