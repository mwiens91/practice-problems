# @leet start
class Solution:
    def findKOr(self, nums: list[int], k: int) -> int:
        result = 0

        for bit in range(max(num.bit_length() for num in nums)):
            bit_set_count = 0

            for num in nums:
                if (num >> bit) & 1 == 1:
                    bit_set_count += 1

                    if bit_set_count == k:
                        result |= 1 << bit

                        break

        return result


# @leet end
