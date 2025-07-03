# @leet start
import heapq


class Solution:
    def minSubsequence(self, nums: list[int]) -> list[int]:
        included_nums: list[int] = []
        included_sum = 0
        remaining_sum = sum(nums)

        # Since heapq operates on min-heaps, we negate all elements
        # while they're in the heap
        heap = [-num for num in nums]
        heapq.heapify(heap)

        while included_sum <= remaining_sum:
            largest_num = -heapq.heappop(heap)

            included_nums.append(largest_num)
            included_sum += largest_num
            remaining_sum -= largest_num

        return included_nums


# @leet end
