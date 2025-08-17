# @leet start
from collections import Counter


class Solution:
    def findMatrix(self, nums: list[int]) -> list[list[int]]:
        counts = Counter(nums)
        result: list[list[int]] = []

        while counts:
            next_row: list[int] = []
            exhausted_nums: list[int] = []

            for num in counts:
                next_row.append(num)

                counts[num] -= 1

                if counts[num] == 0:
                    exhausted_nums.append(num)

            for num in exhausted_nums:
                del counts[num]

            result.append(next_row)

        return result


# @leet end
