# @leet start
from collections import Counter


class Solution:
    def countQuadruplets(self, nums: list[int]) -> int:
        # For each index c with 2 <= c < n - 1 find pair differences
        # nums[d] - nums[c] with c < d < n
        n = len(nums)
        pair_diffs = {
            c: Counter(nums[d] - nums[c] for d in range(c + 1, n))
            for c in range(2, n - 1)
        }

        # We need to find all occurances of
        # nums[a] + nums[b] + nums[c] == nums[d], with a < b < c < d.
        # This is equivalent to finding all occurances of
        # nums[a] + nums[b] == nums[d] - nums[c], with a < b < c < d.
        # To find all such occurances, we sum all occurances for each
        # index b in the second expression, with 1 <= b < n - 2.
        count = 0
        available_diffs = sum(pair_diffs.values(), Counter())

        for b in range(1, n - 2):
            # For each pair sum nums[a] + nums[b] with a < b, add the
            # count of pair differences matching this sum
            for a in range(b):
                count += available_diffs[nums[a] + nums[b]]

            # Set up for the next iteration, removing the pair
            # differences involving the next index b + 1 from the
            # available pair differences
            available_diffs -= pair_diffs[b + 1]

        return count


# @leet end
