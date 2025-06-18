# @leet start
from collections import Counter


class Solution:
    def isGood(self, nums: list[int]) -> bool:
        max_num = max(nums)
        nums_counter = Counter(nums)

        # Assert all nums 1 -> max_num - 1 have count 1
        for x in range(1, max_num):
            try:
                assert nums_counter[x] == 1
            except (IndexError, AssertionError):
                return False

        # Assert max_num has count 2
        try:
            assert nums_counter[max_num] == 2
        except AssertionError:
            return False

        return True


# @leet end
