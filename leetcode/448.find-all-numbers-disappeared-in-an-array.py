# @leet start
class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        # This is an O(n) time, O(1) space solution. To simplify the
        # problem assume the list is 1-indexed. For the first index 1,
        # we visit the index corresponding to nums[1] and mark that
        # index with 0, then we visit the index corresponding to
        # nums[nums[1]] and mark that index with 0, and we keep
        # repeating this process until we reach a number that has
        # 0. Then we move to the next index (2, in this case), if the
        # element at index 2 is 0, we've already visited this index, so
        # we continue to the next index; otherwise, we perform the
        # process above.
        ALREADY_PROCESSED = 0

        for i, num in enumerate(nums):
            if num == ALREADY_PROCESSED:
                continue

            current_idx = num - 1

            while nums[current_idx] != ALREADY_PROCESSED:
                next_idx = nums[current_idx] - 1
                nums[current_idx] = ALREADY_PROCESSED
                current_idx = next_idx

        return [i + 1 for i, num in enumerate(nums) if num != ALREADY_PROCESSED]


# @leet end
