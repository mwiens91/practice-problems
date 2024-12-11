# @leet start
class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        # Use recursion here
        combinations = []

        def recurse(elements: list[int]) -> None:
            # Current length
            num_elements_left = k - len(elements)

            # Base case
            if not num_elements_left:
                combinations.append(elements)

                return

            # Generate combinations
            start_num = 0 if not elements else elements[-1]

            # The fancy end range is set up to avoid computing
            # combinations that won't end up working (e.g, k = 3,
            # elements = [1, n]—can't add anything more here)
            for x in range(start_num + 1, n - num_elements_left + 2):
                recurse(elements + [x])

        recurse([])

        return combinations


# @leet end
