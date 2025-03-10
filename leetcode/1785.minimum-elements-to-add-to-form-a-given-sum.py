# @leet start
class Solution:
    def minElements(self, nums: list[int], limit: int, goal: int) -> int:
        # Get the absolute value of the effective goal we need new elements to reach
        abs_effective_goal = abs(goal - sum(nums))

        # Count the number of numbers we need to add. We try to add as
        # many elements with the limit value as possible. Then we
        # possibly add another element if the limit does not divide the
        # absolute effective goal.
        count = abs_effective_goal // limit

        if abs_effective_goal % limit != 0:
            count += 1

        return count


# @leet end
