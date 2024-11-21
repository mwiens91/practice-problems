# @leet start
from collections import Counter


class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        # This is similar to subsets I (and subsets I and II are *super*
        # similar to another two problems I've done before—not going to
        # bother to look that up though)

        # First we're going to get a count of each num in nums and a
        # list of distinct nums
        counts = Counter(nums)
        distinct_nums = list(counts.keys())

        num_distinct = len(distinct_nums)

        # Next iterate over all distinct nums using recursion, using
        # each num at most as many times as its count
        results = []

        def recurse(
            idx: int = 0, idx_used_count: int = 0, curr_list: list[int] = []
        ) -> None:
            # Base case
            if idx == num_distinct:
                results.append(curr_list)

                return

            # Recurse, once with this index (if possible), once without it
            this_num = distinct_nums[idx]

            if idx_used_count < counts[this_num]:
                recurse(idx, idx_used_count + 1, curr_list + [this_num])

            recurse(idx + 1, 0, curr_list)

        recurse()

        return results


# @leet end
