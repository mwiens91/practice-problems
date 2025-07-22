# @leet start
class Solution:
    def numberOfPoints(self, nums: list[list[int]]) -> int:
        # We can do this in O(n) because the constraints are so small
        MAX_END = 100

        cover_change = [0] * (MAX_END + 1)

        for start, end in nums:
            cover_change[start] += 1

            if end < MAX_END:
                cover_change[end + 1] -= 1

        # Find all points that are covered by a car
        num_cars_covering = 0
        covered_points = 0

        for change_point in cover_change:
            num_cars_covering += change_point

            if num_cars_covering > 0:
                covered_points += 1

        return covered_points


# @leet end
