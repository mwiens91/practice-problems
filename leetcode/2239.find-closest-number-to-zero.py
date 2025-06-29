# @leet start
class Solution:
    def findClosestNumber(self, nums: list[int]) -> int:
        closest_num_to_zero = nums[0]
        closest_distance_to_zero = abs(closest_num_to_zero)

        for num in nums:
            distance_to_zero = abs(num)

            if distance_to_zero < closest_distance_to_zero:
                closest_num_to_zero = num
                closest_distance_to_zero = distance_to_zero
            elif distance_to_zero == closest_distance_to_zero:
                # Prefer the positive number if we have 2 distinct
                # equidistant numbers from zero
                closest_num_to_zero = max(closest_num_to_zero, num)

        return closest_num_to_zero


# @leet end
