# @leet start
import heapq


class Solution:
    def largestSumAfterKNegations(self, nums: list[int], k: int) -> int:
        result = sum(nums)

        # Flip the sign of at most k negative numbers, in order from
        # most negative to least negative
        heap = nums.copy()
        heapq.heapify(heap)

        while heap and heap[0] < 0 and k > 0:  # pylint: disable=chained-comparison
            result -= 2 * heapq.heappop(heap)
            k -= 1

        # If there are any negations left (k > 0), all numbers are now
        # positive. If there are an odd number of negations left, negate
        # the number with smallest absolute value
        if k % 2 == 1:
            result -= 2 * min(map(abs, nums))

        return result


# @leet end
