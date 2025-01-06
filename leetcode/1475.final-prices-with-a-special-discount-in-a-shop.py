# @leet start
class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        # We'll store the answer in the original array to make this an
        # O(1) memory approach. I'm not sure if there's a better time
        # complexity than the O(n^2) brute force solution I'm doing
        # here.
        n = len(prices)
        for i in range(n - 1):
            # Get discount if it exists
            discount = 0

            for j in range(i + 1, n):
                if prices[j] <= prices[i]:
                    discount = prices[j]

                    break

            # Store discounted price
            if discount:
                prices[i] -= discount

        return prices


# @leet end
