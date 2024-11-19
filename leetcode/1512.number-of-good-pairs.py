# @leet start
class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        # Keep track of a running count of what characters we've seen
        counts = {}

        # Hold our result here
        result = 0

        for num in nums:
            if num in counts:
                result += counts[num]

                counts[num] += 1
            else:
                counts[num] = 1

        return result


# @leet end
