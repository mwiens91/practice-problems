# @leet start
class Solution:
    def evenOddBit(self, n: int) -> list[int]:
        even_count = 0
        odd_count = 0
        i = 0

        while n:
            if n & 1:
                if i % 2 == 0:
                    even_count += 1
                else:
                    odd_count += 1

            n >>= 1
            i += 1

        return [even_count, odd_count]


# @leet end
