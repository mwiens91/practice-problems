# @leet start
from functools import cmp_to_key


class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        if all(num == 0 for num in nums):
            return "0"

        def cmp(a: str, b: str) -> str:
            if a + b > b + a:
                return 1

            if a + b < b + a:
                return -1

            return 0

        return "".join(
            sorted((str(num) for num in nums), key=cmp_to_key(cmp), reverse=True)
        )


# @leet end
