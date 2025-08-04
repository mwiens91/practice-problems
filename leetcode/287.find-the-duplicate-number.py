# @leet start
class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        # NOTE: I needed ChatGPT to understand that tortoise and hare
        # algorithm works here
        slow = nums[nums[0]]
        fast = nums[nums[nums[0]]]

        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        new_slow = nums[0]

        while new_slow != slow:
            slow = nums[slow]
            new_slow = nums[new_slow]

        return slow


# @leet end
