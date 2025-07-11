# @leet start
class Solution:
    def minBitwiseArray(self, nums: list[int]) -> list[int]:
        # NOTE: Same solution as LC 3314. See that code for comments.
        def find_minimal_consecutive_or_component(n: int) -> int:
            if n % 2 == 0:
                return -1

            for bit in range(1, n.bit_length() + 1):
                if n >> bit & 1 == 0:
                    return n & ~(1 << (bit - 1))

        return list(map(find_minimal_consecutive_or_component, nums))


# @leet end
