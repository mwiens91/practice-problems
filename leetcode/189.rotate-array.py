# @leet start
from math import gcd


class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Use number theory result: the first gcd(n, k) indices are part
        # of unique cycles and all of the cycles together traverse the
        # whole array
        n = len(nums)

        for start_idx in range(gcd(n, k)):
            # Move the value under the current index to its destination,
            # then move the val that was at the destination index to
            # *its* destination, and keep going until we hit a cycle
            val = nums[start_idx]
            next_idx = (start_idx + k) % n

            while next_idx != start_idx:
                next_val = nums[next_idx]
                nums[next_idx] = val

                val = next_val
                next_idx = (next_idx + k) % n

            nums[next_idx] = val


# @leet end
