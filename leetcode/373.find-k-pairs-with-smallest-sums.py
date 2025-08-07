# @leet start
import heapq


class Solution:
    def kSmallestPairs(
        self, nums1: list[int], nums2: list[int], k: int
    ) -> list[list[int]]:
        # NOTE: Needed ChatGPT to figure out how to optimize this

        # In a heap we'll keep tuples (nums1[i] + nums2[j], i, j) such
        # that 0 <= i < k and j is the smallest index for this i that
        # hasn't already been used
        n1 = len(nums1)
        n2 = len(nums2)

        heap: list[tuple[int, int, int]] = []

        for i in range(min(k, n1)):
            heapq.heappush(heap, (nums1[i] + nums2[0], i, 0))

        result: list[list[int]] = []

        while len(result) < k:
            _, i, j = heapq.heappop(heap)
            result.append([nums1[i], nums2[j]])

            if j < n2 - 1:
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))

        return result


# @leet end
