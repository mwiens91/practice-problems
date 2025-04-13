# @leet start
class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        # Get the number of unique elements in nums and the smallest
        # element
        nums_set = set(nums)

        num_unique_nums = len(nums_set)
        min_num = min(nums_set)

        # Let N be the number of unique elements in nums. If k is larger
        # than the smallest element, we cannot make all values equal to
        # k. If k is equal to the smallest element, we need N - 1
        # operations. If k is smaller than the smallest element, we need
        # N operations.
        if k > min_num:
            return -1

        if k == min_num:
            return num_unique_nums - 1

        return num_unique_nums


# @leet end
