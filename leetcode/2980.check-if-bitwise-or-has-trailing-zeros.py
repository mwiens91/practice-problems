# @leet start
class Solution:
    def hasTrailingZeros(self, nums: list[int]) -> bool:
        seen_one_trailing_zero = False

        for num in nums:
            if num & 1 == 0:
                if seen_one_trailing_zero:
                    return True

                seen_one_trailing_zero = True

        return False


# @leet end
