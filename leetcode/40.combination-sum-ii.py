# @leet start
from collections import Counter


class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        # Count the number of occurances of each candidate. Using this
        # counter, all we need to do is modify the combination sum I
        # problem solution slightly.
        candidate_counter = Counter(candidates)

        # Get the distinct candidates
        distinct_candidates = list(candidate_counter.keys())
        n_distinct = len(distinct_candidates)

        # Store the results here
        combinations = []

        # Define a recursive function to generate unique combinations
        # that sum to target. There might be a fancier way of solving
        # this problem, but this works.
        def recurse(
            idx: int = 0,
            times_index_used: int = 0,
            current_sum: int = 0,
            nums: list[int] = [],
        ) -> None:
            # Base case: if we're >= target
            if current_sum >= target:
                if current_sum == target:
                    combinations.append(nums)

                return

            # Try adding the candidate this index points to the current
            # sum, or move to the next index
            this_num = distinct_candidates[idx]

            if times_index_used < candidate_counter[this_num]:
                recurse(
                    idx, times_index_used + 1, current_sum + this_num, nums + [this_num]
                )

            if idx < n_distinct - 1:
                recurse(idx + 1, 0, current_sum, nums)

        # Recurse
        recurse()

        return combinations


# @leet end
