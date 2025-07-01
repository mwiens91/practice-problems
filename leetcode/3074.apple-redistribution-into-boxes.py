# @leet start
class Solution:
    def minimumBoxes(self, apple: list[int], capacity: list[int]) -> int:
        remaining_capacity_needed = sum(apple)

        for i, this_capacity in enumerate(sorted(capacity, reverse=True)):
            remaining_capacity_needed -= this_capacity

            if remaining_capacity_needed <= 0:
                return i + 1


# @leet end
