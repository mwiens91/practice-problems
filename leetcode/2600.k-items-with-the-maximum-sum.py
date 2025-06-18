# @leet start
class Solution:
    def kItemsWithMaximumSum(
        self,
        numOnes: int,
        numZeros: int,
        numNegOnes: int,  # pylint: disable=unused-argument
        k: int,
    ) -> int:
        max_sum = 0

        # Get the k greatest items
        items_remaining = k

        # Take 1s first
        ones_to_take = min(numOnes, items_remaining)

        items_remaining -= ones_to_take
        max_sum += ones_to_take

        # Take 0s next
        items_remaining -= min(numZeros, items_remaining)

        # Take 1s next
        max_sum -= items_remaining

        return max_sum


# @leet end
