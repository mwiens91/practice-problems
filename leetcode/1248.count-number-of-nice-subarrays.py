# @leet start
class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        # For each odd number we're going to count how many consecutive
        # even numbers come directly before it and how many come after
        # it; these will be in a tuple, and each tuple will represent
        # an odd number
        odd_number_counts: list[tuple[int, int]] = []

        # First find index of first odd number
        num_nums = len(nums)
        last_odd_idx = 0

        while last_odd_idx < num_nums and nums[last_odd_idx] % 2 == 0:
            last_odd_idx += 1

        # Now iteratively find number of even numbers before and after
        # each odd number
        num_even_before = last_odd_idx

        while last_odd_idx < num_nums:
            # Move to either the end of the array or the next odd number
            idx = last_odd_idx + 1

            while idx < num_nums and nums[idx] % 2 == 0:
                idx += 1

            # Append the number of even numbers before and after to our
            # counts list
            num_even_after = idx - last_odd_idx - 1

            odd_number_counts.append((num_even_before, num_even_after))

            # Set up for next odd number
            last_odd_idx = idx
            num_even_before = num_even_after

        # For each group of k consecutive odd numbers the number of nice
        # subarrays contributed by this group is equal to 1 + the number
        # of even numbers preceding the first odd number of the group
        # multiplied by 1 + the number of even numbers proceeding the
        # final odd number of the group
        num_nice_subarrays = 0

        # The index we iterate over is an index to odd_number_counts
        for final_odd_in_group_idx in range(k - 1, len(odd_number_counts)):
            first_num_in_group_counts = odd_number_counts[
                final_odd_in_group_idx - k + 1
            ]
            final_num_in_group_counts = odd_number_counts[final_odd_in_group_idx]

            num_nice_subarrays += (1 + first_num_in_group_counts[0]) * (
                1 + final_num_in_group_counts[1]
            )

        return num_nice_subarrays


# @leet end
