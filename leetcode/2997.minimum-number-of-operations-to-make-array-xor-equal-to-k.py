# @leet start
class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        for num in nums:
            k ^= num

        return k.bit_count()


# @leet end
