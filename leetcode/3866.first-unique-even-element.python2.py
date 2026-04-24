# @leet start
class Solution(object):
    def firstUniqueEven(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freqs = [0] * 101

        for num in nums:
            freqs[num] += 1

        for num in nums:
            if num % 2 == 0 and freqs[num] == 1:
                return num

        return -1


# @leet end
