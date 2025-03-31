# @leet start
import heapq


class Solution:
    def putMarbles(self, weights: list[int], k: int) -> int:
        # We need to place k - 1 boundaries where one partition (bag)
        # ends and the next begins. Note that the last index is never a
        # boundary.
        #
        # We need to return the difference between the maximum and
        # minimum scores among the bag distributions. The score of any
        # distribution is the sum of its boundary costs plus the weight
        # of the first element and last element. To find the difference
        # between the maximum and minimum scores, we thus only need to
        # find the difference between the maximum k - 1 boundary costs
        # and the minimum k - 1 boundary costs.
        #
        # We'll have two heaps, a "smallest heap" which keeps tracks of
        # the smallest boundary costs, and a "largest heap" which keeps
        # track of the largest boundary costs. Python's heapq operates
        # on min-heaps. In the "smallest heap" we will need to push the
        # smallest elements and pop the largest; in order to do this, we
        # store the negative of the boundary costs. Similarly, for the
        # "largest heap" we store the positive boundary costs so we can
        # pop the smallest
        smallest_heap = []
        largest_heap = []

        for i in range(k - 1):
            boundary_cost = weights[i] + weights[i + 1]

            heapq.heappush(smallest_heap, -boundary_cost)
            heapq.heappush(largest_heap, boundary_cost)

        for i in range(k - 1, len(weights) - 1):
            boundary_cost = weights[i] + weights[i + 1]

            heapq.heappushpop(smallest_heap, -boundary_cost)
            heapq.heappushpop(largest_heap, boundary_cost)

        # We need the difference between the largest boundary costs and
        # the smallest, but all elements in the smallest heap are
        # already negative, so we can just add the sum of the heaps
        # together
        return sum(largest_heap) + sum(smallest_heap)


# @leet end
