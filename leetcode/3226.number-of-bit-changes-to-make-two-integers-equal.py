# @leet start
class Solution:
    def minChanges(self, n: int, k: int) -> int:
        # Count number of bits that need to be unset in nso that n and k
        # have the same set bits. If k has any set bits that aren't set
        # in n, this is impossible.
        if k > n:
            return -1

        count = 0

        while n:
            n_bit = n & 1
            k_bit = k & 1

            if not n_bit and k_bit:
                return -1

            if n_bit and not k_bit:
                count += 1

            n >>= 1
            k >>= 1

        return count


# @leet end
