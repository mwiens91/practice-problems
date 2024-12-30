# @leet start
class Solution:
    def fairCandySwap(self, aliceSizes: list[int], bobSizes: list[int]) -> list[int]:
        # Get number more candies Alice has than Bob
        alice_bob_candy_delta = sum(aliceSizes) - sum(bobSizes)

        unique_alice_sizes = set(aliceSizes)
        unique_bob_sizes = set(bobSizes)

        # For each size box Alice has, see if Bob has a box he can trade
        # to make things equal
        for alice_gift_size in unique_alice_sizes:
            required_bob_gift_size = alice_gift_size - alice_bob_candy_delta / 2

            if required_bob_gift_size in unique_bob_sizes:
                return [alice_gift_size, required_bob_gift_size]


# @leet end
