# @leet start
import math


class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        return 100 - math.floor(purchaseAmount / 10 + 0.5) * 10


# @leet end
