# @leet start
class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        # Get the number of candidates
        n = len(candidates)

        # Store the results here
        combinations = []

        # Define a recursive function to generate unique combinations
        # that sum to target. There might be a fancier way of solving
        # this problem, but this works.
        def recurse(idx: int = 0, current_sum: int = 0, nums: list[int] = []) -> None:
            # Base case: if we're >= target
            if current_sum >= target:
                if current_sum == target:
                    combinations.append(nums)

                return

            # Try adding the candidate this index points to the current
            # sum, or move to the next index (but don't add it to the
            # current sum yet—this ensures that we'll get all valid
            # combinations)
            this_num = candidates[idx]

            recurse(idx, current_sum + this_num, nums + [this_num])

            if idx < n - 1:
                recurse(idx + 1, current_sum, nums)

        # Recurse
        recurse()

        return combinations


# @leet end
