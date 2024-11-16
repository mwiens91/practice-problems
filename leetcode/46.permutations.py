# @leet start
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        # Store results in a list
        results = []

        # Define recursive function to generate permutations
        def recurse(nums_to_add: list, accum: list) -> None:
            # Base case
            if not nums_to_add:
                results.append(accum)

            # Generate permutations
            for i, x in enumerate(nums_to_add):
                recurse(nums_to_add[:i] + nums_to_add[i + 1 :], accum + [x])

        # Return all permutations
        recurse(nums, [])

        return results


# @leet end
