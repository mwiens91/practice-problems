# @leet start
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        # NOTE: It feels like there might be a closed-form formula for
        # this, possible to do in O(1) time?
        num_empty = numBottles
        num_drank = numBottles

        # Exchange and drink as many times as possible
        while num_empty >= numExchange:
            num_new = num_empty // numExchange
            num_drank += num_new

            num_empty = num_new + num_empty % numExchange

        return num_drank


# @leet end
