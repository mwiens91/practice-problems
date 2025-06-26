# @leet start
class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        # Find the indices of the 1s bits and the number of trailing
        # zero bits
        one_bit_idxs = [i for i, bit in enumerate(s) if bit == "1"]

        # Get the value of the digit
        n = len(s)
        val = 0

        for i in one_bit_idxs:
            val += 1 << (n - 1 - i)

        # Remove the most significant 1 bits in order until the value is
        # <= k
        subseq_length = n
        removal_idx = 0

        while val > k and removal_idx < len(one_bit_idxs):
            val -= 1 << (n - 1 - one_bit_idxs[removal_idx])

            subseq_length -= 1
            removal_idx += 1

        return subseq_length


# @leet end
