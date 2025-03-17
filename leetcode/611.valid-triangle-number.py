# @leet start
class Solution:
    def triangleNumber(self, nums: list[int]) -> int:
        # NOTE: this is heavily ripping off the LeetCode editorial
        # solution. I'm not copying exactly, but the solution idea is
        # mostly the same.

        # First, sort the nums
        nums.sort()

        # A triangle is valid provided that (1) the largest side is
        # smaller than the sum of the other two sides and (2) none of
        # the sides are 0 length
        valid_triangle_count = 0

        # For each index i pointing to the smallest length side of a
        # given triangle, count the number of valid triangles that can
        # be made using this number
        n = len(nums)

        for i in range(n - 2):
            # Skip past any 0-length sides
            if nums[i] == 0:
                continue

            # k points to the largest length side
            k = i + 2

            # j will point to the middle length side
            for j in range(i + 1, n - 1):
                sum_of_smaller_sides = nums[i] + nums[j]

                # Do a binary search to move k to the smallest index
                # such that for all numbers k' between j + 1 (inclusive)
                # and k (exclusive), nums[k'] < sum_of_smaller_sides
                left = k
                right = n - 1

                while left <= right:
                    mid = (left + right) // 2

                    if nums[mid] < sum_of_smaller_sides:
                        left = mid + 1
                    else:
                        right = mid - 1

                k = left

                # All larger sides between j + 1 and k - 1 work to make
                # a valid triangle
                valid_triangle_count += k - j - 1

        return valid_triangle_count


# @leet end
