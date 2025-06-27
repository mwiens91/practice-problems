# @leet start
from collections.abc import Iterator
import itertools


class Solution:
    def sumIndicesWithKSetBits(self, nums: list[int], k: int) -> int:
        max_idx = len(nums) - 1
        max_bits = max_idx.bit_length()

        def generate_idxs_with_k_bits_set() -> Iterator[int]:
            for set_bits in itertools.combinations(range(max_bits), k):
                idx = 0

                for bit in set_bits:
                    idx |= 1 << bit

                if idx <= max_idx:
                    yield idx

        return sum(nums[i] for i in generate_idxs_with_k_bits_set())


# @leet end
