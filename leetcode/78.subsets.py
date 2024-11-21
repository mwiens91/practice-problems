# @leet start
class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        # Number of nums
        n = len(nums)

        # Keep results here
        results = []

        # We'll have a recursive solution where for each num, we either
        # take it or we don't. This will give us all possible
        # combinations.
        def recurse(idx: int = 0, curr_list: list[int] = []) -> None:
            # Base case
            if idx == n:
                results.append(curr_list)

                return

            # Recurse, once with this element, once without it
            recurse(idx + 1, curr_list + [nums[idx]])
            recurse(idx + 1, curr_list)

        # Get and return results
        recurse()

        return results


# @leet end
