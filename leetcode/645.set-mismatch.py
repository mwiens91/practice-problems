# @leet start
class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        # Make a set of all numbers from 1 to n. We'll remove elements
        # from this set as we iterate through nums. We'll also find
        # which element occurs twice.
        all_nums = set(range(1, len(nums) + 1))

        for num in nums:
            try:
                all_nums.remove(num)
            except KeyError:
                # num already removed. This is the element occuring
                # twice
                duplicate_element = num

        missing_element = next(iter(all_nums))

        return [
            duplicate_element,  # pylint: disable=used-before-assignment
            missing_element,
        ]


# @leet end
