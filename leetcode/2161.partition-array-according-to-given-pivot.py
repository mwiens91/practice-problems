# @leet start
class Solution:
    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:
        # Put all numbers less than or greater than the pivot into
        # lists, preserving relative order
        less_than_pivot_nums = []
        more_than_pivot_nums = []

        # Count the number of pivot elements
        pivot_count = 0

        for num in nums:
            if num < pivot:
                less_than_pivot_nums.append(num)
            elif num > pivot:
                more_than_pivot_nums.append(num)
            else:
                pivot_count += 1

        return less_than_pivot_nums + [pivot] * pivot_count + more_than_pivot_nums


# @leet end
