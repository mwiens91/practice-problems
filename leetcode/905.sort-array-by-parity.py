# @leet start
class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        # It's simpler and probably faster to do this in O(n) memory,
        # but I'm going to do it in O(1) memory
        even_count = sum(1 for num in nums if num % 2 == 0)

        odd_insert_ptr = even_count

        for i in range(even_count):
            if nums[i] % 2 == 1:
                # Move the odd insertion pointer to an even number. If
                # we get here there is guaranteed to be one.
                while nums[odd_insert_ptr] % 2 == 1:
                    odd_insert_ptr += 1

                nums[i], nums[odd_insert_ptr] = nums[odd_insert_ptr], nums[i]

                odd_insert_ptr += 1

        return nums


# @leet end
