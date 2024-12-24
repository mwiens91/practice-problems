# @leet start
class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        # We'll construct a counter which has numbers that appear in
        # either array as keys and corresponding lists of integers
        # containing counts for those keys in one or both arrays as
        # values
        total_counts: dict[int, list[int]] = {}

        for array in [nums1, nums2]:
            # Get counts for this array
            array_counts: dict[int, int] = {}

            for num in array:
                if num in array_counts:
                    array_counts[num] += 1
                else:
                    array_counts[num] = 1

            # Put these counts in the counter for both arrays
            for num, count in array_counts.items():
                if num in total_counts:
                    total_counts[num].append(count)
                else:
                    total_counts[num] = [count]

        # Build the output intersection array
        res = []

        for num, counts_list in total_counts.items():
            # Only include elements found in both lists
            if len(counts_list) > 1:
                # Include the minimum number of the element found in
                # either list
                res += [num] * min(counts_list)

        return res


# @leet end
