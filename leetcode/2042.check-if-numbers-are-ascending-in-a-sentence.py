# @leet start
import re


class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        # Get all numbers
        nums = re.findall(r"\d+", s)

        # Handle 0 or 1 numbers
        if len(nums) <= 1:
            return True

        # Return False if any non-ascending, else return True
        prev = int(nums[0])

        for num in [int(x) for x in nums[1:]]:
            if num <= prev:
                return False

            prev = num

        return True


# @leet end
