# @leet start
class Solution:
    def hasIncreasingSubarrays(self, nums: list[int], k: int) -> bool:
        # Handle edge case
        if k == 1:
            return True

        # If any given run of strictly increasing elements is >= 2*k or
        # any adjacent runs are both >= k, then the answer is True,
        # otherwise False
        prev_run_length = 0
        current_run_length = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                current_run_length += 1

                if (
                    current_run_length >= 2 * k
                    or prev_run_length >= k
                    and current_run_length >= k
                ):
                    return True
            else:
                prev_run_length = current_run_length
                current_run_length = 1

        return False


# @leet end
