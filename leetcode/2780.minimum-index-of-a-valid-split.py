# @leet start
class Solution:
    def minimumIndex(self, nums: list[int]) -> int:
        # Get the dominant element and the number of times it occurs in
        # nums. Use Moore's algorithm.
        dominant_elem = None
        count = 0

        for num in nums:
            if count == 0:
                dominant_elem = num

            count += 1 if num == dominant_elem else -1

        # Count the occurances of the dominant element. Note that the
        # count used in the above algorithm is not the *actual* count of
        # the dominant element.
        total_count = nums.count(dominant_elem)

        # Split nums with an index i, such that i belongs to the left
        # split and i + 1 belongs to the right. Find the first index i
        # such that the dominant element is dominant in both left and
        # right subarrays.
        n = len(nums)

        left_count = 0

        for i in range(n - 1):
            left_count += int(nums[i] == dominant_elem)

            # See if the dominant element is dominant in each split
            right_count = total_count - left_count

            if left_count / (i + 1) > 1 / 2 and right_count / (n - i - 1) > 1 / 2:
                return i

        # No valid split possible
        return -1


# @leet end
