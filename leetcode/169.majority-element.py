# @leet start
import itertools

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        # NOTE: For O(1) space solution I needed to see Neetcode's
        # solution

        # Get the first element as our candidate and iterate through the
        # rest of the array
        candidate_elem = nums[0]
        count = 1

        # The procedure we will use is as follows: for each index
        # 1 < i < n and corresponding element num_i, if num_i is the
        # candidate element, then increment the count; otherwise,
        # decrement the count. If the count reaches zero, then num_i is
        # the new candidate element with count 1. It shouldn't be too
        # difficult to prove this (I think?) but it should hopefully be
        # intuitive that for a majority element x, because x appears
        # more than half the time, by the time we finish iterating over
        # the entire array, the candidate element we are left with will
        # be x. This is because more than half of the counts will
        # contribute towards x, and the other counts cannot overtake
        # this.

        for num in itertools.islice(nums, 1, len(nums)):
            if num == candidate_elem:
                count += 1
            else:
                count -= 1

                if count == 0:
                    candidate_elem = num
                    count = 1

        return candidate_elem
# @leet end
