# @leet start
class Solution:
    def alternatingSubarray(self, nums: list[int]) -> int:
        max_length = -1

        current_length = -1
        nums_to_alternate: tuple[int, int] = ()

        for num, next_num in zip(nums, nums[1:]):
            if current_length > 0:
                if next_num == nums_to_alternate[current_length % 2]:
                    # Extend current alternating subarrray
                    current_length += 1
                else:
                    # End current alternating subarray
                    max_length = max(max_length, current_length)

                    current_length = 0

            if current_length <= 0 and next_num == num + 1:
                # Start new alternating subarray
                current_length = 2
                nums_to_alternate = (num, next_num)

        # Do final update on max length
        max_length = max(max_length, current_length)

        return max_length


# @leet end
