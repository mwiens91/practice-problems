# @leet start
import heapq


class Solution:
    def maximumProduct(self, nums: list[int]) -> int:
        # The maximum product is either the three largest numbers
        # multiplied together or the two smallest multiplied together
        # with the largest number. It's trivial to see that this is true
        # when we have more than 3 positive and more than 3 negative
        # numbers. When we have less than these counts, this is still
        # true, but it's less easy to see. Proof not included :(
        largest = heapq.nlargest(3, nums)
        smallest = heapq.nsmallest(2,nums)

        return max(largest[0] * largest[1] * largest[2], smallest[0]* smallest[1] * largest[0])


# @leet end
