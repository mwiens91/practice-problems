# @leet start
class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        # We'll keep track of the last seen index of numbers we've seen
        # so far in a dictionary. This let's us do this with O(n) time
        # and memory complexity
        nums_last_seen_index_dict: dict[int, int] = {}

        for i, num in enumerate(nums):
            if num in nums_last_seen_index_dict:
                # First encounter
                nums_last_seen_index_dict[num] = i
            else:
                # We've seen this before
                if i - nums_last_seen_index_dict[num] <= k:
                    return True

                # Update the last seen index
                nums_last_seen_index_dict[num] = i

        return False


# @leet end
