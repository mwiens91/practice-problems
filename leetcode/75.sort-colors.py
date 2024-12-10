# @leet start
class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Idea: move all 0s to the front, then for the subarray
        # after the 0s, move all the 1s to the front
        n = len(nums)

        def move_xs_to_front(start: int, end: int, x: int) -> int:
            """Moves integers x to the front of subarray

            Returns the first index after which all elemenets are non-x.
            """
            while start < end:
                if nums[start] == x:
                    start += 1
                elif nums[end] != x:
                    end -= 1
                else:
                    nums[start], nums[end] = nums[end], nums[start]

            return start

        first_non_zero_idx = move_xs_to_front(0, n - 1, 0)
        move_xs_to_front(first_non_zero_idx, n - 1, 1)


# @leet end
