# @leet start
class Solution(object):
    def minDistinctFreqPair(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        freqs = [0] * 101

        for num in nums:
            freqs[num] += 1

        uniq_ordered_nums = sorted(set(nums))

        for i, x in enumerate(uniq_ordered_nums):
            for j in range(i + 1, len(uniq_ordered_nums)):
                y = uniq_ordered_nums[j]

                if freqs[x] != freqs[y]:
                    return [x, y]

        return [-1, -1]


# @leet end
