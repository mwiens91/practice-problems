# @leet start
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        # Length of nums
        n = len(nums)

        # Number of duplicates we allow for
        MAX_DUPLICATES = 2

        # We'll do this in two passes: first we'll mark which elements
        # we need to remove
        TO_REMOVE = None

        curr_num = nums[0]
        count = 0

        # Keep track of the very first index we need to remove
        to_remove_index = None

        # Keep track of the number of elements we need to remove
        num_elements_removed = 0

        for i, num in enumerate(nums):
            if num == curr_num:
                # Continuing from prev num
                if count >= MAX_DUPLICATES:
                    if to_remove_index is None:
                        to_remove_index = i

                    nums[i] = TO_REMOVE

                    num_elements_removed += 1
                else:
                    count += 1
            else:
                # New num
                curr_num = num
                count = 1

        # If we didn't have anything to remove, then we can exit out now
        if to_remove_index is None:
            return n

        # Now with all elements marked, we'll move elements forward to
        # remove the duplicates
        to_keep_index = to_remove_index + 1

        # Instead of doing lots of checks to make sure the indices are
        # valid, we'll just let them fail when they are invalid and
        # catch the error. This works because whenever the indices
        # become invalid for this, it means we're finished.
        try:
            while True:
                # Make sure to_keep_index points to an element to keep
                while nums[to_keep_index] == TO_REMOVE:
                    to_keep_index += 1

                # Swap in the element to keep
                nums[to_remove_index] = nums[to_keep_index]

                to_remove_index += 1
                to_keep_index += 1
        except IndexError:
            pass

        # Return the number of elements kept in our array
        return n - num_elements_removed


# @leet end
