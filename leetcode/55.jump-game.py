# @leet start
class Solution:
    def canJump(self, nums: list[int]) -> bool:
        # Idea here: for any zeros we encounter, we need to make sure we
        # can jump over it. Can do this in one pass with constant
        # memory.
        current_max_jump = 0

        for num in nums:
            if num == 0:
                # Handle 0 here
                if current_max_jump < 2:
                    return False

            # Update current maximum jump distance
            current_max_jump = max(current_max_jump - 1, num)

        return True


# @leet end
