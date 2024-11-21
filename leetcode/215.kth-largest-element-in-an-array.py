# @leet start
import heapq


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        # heapq supports min heaps, so to have a max heap we need to
        # take the negative of all the numbers. I'll modify the input
        # array so we can make this O(1) memory.

        # Negate the input
        for i, num in enumerate(nums):
            nums[i] = -num

        # Heapify the input
        heapq.heapify(nums)

        # Get the kth largest element. We're going to negate the return
        # value again.
        for _ in range(k - 1):
            heapq.heappop(nums)

        return -heapq.heappop(nums)


# @leet end
