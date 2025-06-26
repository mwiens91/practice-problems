# @leet start
from collections import defaultdict


class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        # Count the number of excess numbers we need to get rid of
        nums_seen: set[int] = set()
        counts_over_one: defaultdict[int, int] = defaultdict(int)

        for num in nums:
            if num in nums_seen:
                counts_over_one[num] += 1
            else:
                nums_seen.add(num)

        # Try removing three elements at a time until we have no excess
        # numbers
        num_operations = 0

        n = len(nums)
        i = 0

        while len(counts_over_one) > 0:
            for _ in range(min(3, n - i)):
                num_to_remove = nums[i]

                if num_to_remove in counts_over_one:
                    counts_over_one[num_to_remove] -= 1

                    if counts_over_one[num_to_remove] == 0:
                        del counts_over_one[num_to_remove]

                i += 1

            num_operations += 1

        return num_operations


# @leet end
