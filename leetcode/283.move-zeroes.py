# @leet start
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Two pointers: back_i will point to the back of the list and
        # we'll move this index towards the front as we push zeros past
        # it; z_i will move from back to front to point to a zero
        # element of the list. Idea: once we find a zero with z_i, move
        # that zero past back_i, so it'll be at the very back.
        nums_len = len(nums)

        back_i = nums_len - 1
        z_i = nums_len - 1

        while z_i >= 0:
            if nums[z_i] == 0:
                # Move the zero to the back
                tmp_i = z_i

                while tmp_i < back_i:
                    tmp_i += 1
                    nums[tmp_i], nums[tmp_i - 1] = nums[tmp_i - 1], nums[tmp_i]

                back_i -= 1

            z_i -= 1

        return nums


# @leet end
