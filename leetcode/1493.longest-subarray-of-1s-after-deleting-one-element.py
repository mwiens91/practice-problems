# @leet start
class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        # Deal with an edge case of all 1s
        if all(num == 1 for num in nums):
            return len(nums) - 1

        result = 0

        # Track the alternating runs of 1s and 0s
        prev_prev_run = 0
        prev_run = 0
        current_run = 0
        current_run_num = nums[0]

        for num in nums:
            if num == current_run_num:
                current_run += 1
            else:
                if current_run_num == 1:
                    # Ended a run of 1s: if the previous run (0s) has
                    # length 1 then we can combine the second previous
                    # run (1s) with the current run
                    result = max(
                        result, current_run + (prev_prev_run if prev_run == 1 else 0)
                    )

                prev_prev_run = prev_run
                prev_run = current_run
                current_run = 1
                current_run_num = num

        # Final update
        if current_run_num == 1:
            result = max(result, current_run + (prev_prev_run if prev_run == 1 else 0))

        return result


# @leet end
