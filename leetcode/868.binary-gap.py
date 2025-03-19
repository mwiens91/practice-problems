# @leet start
class Solution:
    def binaryGap(self, n: int) -> int:
        # First, consume the least significant bits until we encounter a
        # 1 bit
        while True:
            if n & 1 == 1:
                break

            n >>= 1

        # Consume the 1 bit and go through remaining bits in the binary
        # representation of n to find the longest gap
        n >>= 1

        longest_gap = 0
        current_gap = 1

        while n:
            if n & 1 == 1:
                # Update longest gap
                longest_gap = max(longest_gap, current_gap)

                # Reset for next iteration
                current_gap = 1
            else:
                # Increment current gap
                current_gap += 1

            n >>= 1

        return longest_gap


# @leet end
