# @leet start
import itertools


class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        # Put our results here
        results = []

        # Deal with edge case of no nums
        if not nums:
            return []

        # Put contiguous elements in ranges
        first_in_range = nums[0]
        prev_num = nums[0]

        for num in itertools.islice(nums, 1, len(nums)):
            if num != prev_num + 1:
                # Record old range
                if prev_num == first_in_range:
                    # Single digit in range
                    results.append(str(prev_num))
                else:
                    results.append(str(first_in_range) + "->" + str(prev_num))

                # Start new range
                first_in_range = num

            # Update last seen number
            prev_num = num

        # Record the final range
        # TODO: don't copy paste code
        if prev_num == first_in_range:
            # Single digit in range
            results.append(str(prev_num))
        else:
            results.append(str(first_in_range) + "->" + str(prev_num))

        return results


# @leet end
