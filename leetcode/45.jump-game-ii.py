# @leet start
class Solution:
    def jump(self, nums: list[int]) -> int:
        # Store number of jumps taken
        count = 0

        # We'll start from the back, from the final index finding the
        # closest index to the front that jumps there, and continue this
        # process using the new index as we used the final index until
        # we reach the front
        back_index = len(nums) - 1

        while back_index != 0:
            j = back_index - 1

            best_valid_j = None

            while j >= 0:
                # Update the closest to the front j we can take
                required_jumps = back_index - j

                if nums[j] >= required_jumps:
                    best_valid_j = j

                # Try the next index towards the front
                j -= 1

            back_index = best_valid_j
            count += 1

        return count


# @leet end
