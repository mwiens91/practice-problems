# @leet start
class Solution:
    def duplicateNumbersXOR(self, nums: list[int]) -> int:
        seen_once: set[int] = set()

        result = 0

        for num in nums:
            if num in seen_once:
                result ^= num
            else:
                seen_once.add(num)

        return result


# @leet end
