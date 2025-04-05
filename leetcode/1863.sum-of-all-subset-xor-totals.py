# @leet start
class Solution:
    def subsetXORSum(self, nums: list[int]) -> int:
        # The problem states that nums[i] <= 20, so we can represent the
        # answer with 5 bits
        MAX_BITS = 5

        # There are 2^n subsets of nums. If any x in nums has its ith
        # bit set to 1, then in exactly half of these subsets, the XOR
        # of all subsets has the ith bit set to 1 (the other half has
        # the ith bit set to 0). So for each bit i, where at least one
        # element x in nums has its ith bit set to 1, there is a
        # contribution of 2^i to the total. If reach the answer by
        # summing these contributions.
        n = len(nums)

        result = 0

        for i in range(MAX_BITS):
            # (x >> i) & 1 is 1 if the ith bit of x is set to 1, else it
            # is 0
            bit_contributes = any((x >> i) & 1 for x in nums)

            if bit_contributes:
                # 2^i is present in the XOR of half of the 2^n subsets,
                # so it is included 2^(n - 1) times
                result += 2 ** (n - 1 + i)

        return result



# @leet end
