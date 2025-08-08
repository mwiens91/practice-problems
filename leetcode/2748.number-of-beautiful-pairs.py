# @leet start
import math


class Solution:
    def countBeautifulPairs(self, nums: list[int]) -> int:
        n = len(nums)
        count = 0

        for i in range(n):
            nums_i_first_digit = int(str(nums[i])[0])

            for j in range(i + 1, n):
                if math.gcd(nums_i_first_digit, int(str(nums[j])[-1])) == 1:
                    count += 1

        return count


# @leet end
