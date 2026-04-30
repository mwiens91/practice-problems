# @leet start
class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        count = 0

        for num in nums:
            while num:
                num, dig = divmod(num, 10)

                if dig == digit:
                    count += 1

        return count


# @leet end
