# @leet start
class Solution:
    def countLargestGroup(self, n: int) -> int:
        # A group is a set of numbers <= n whose digits sum to the same
        # number. We want to keep track of the largest group size and
        # the count of how many groups have that size.
        largest_group_size = 0
        count_with_largest_size = 0

        # Dictionary where the keys are digit sums and the values are
        # the sizes of groups corresponding to the key
        digit_sum_group_sizes: dict[int, int] = {}

        for x in range(1, n + 1):
            # Get the digit sum and increase the group size
            digit_sum = sum(int(y) for y in str(x))

            if digit_sum in digit_sum_group_sizes:
                digit_sum_group_sizes[digit_sum] += 1
            else:
                digit_sum_group_sizes[digit_sum] = 1

            # Reset largest size and count if this is now the largest
            # group size, add to the count corresponding to the largest
            # group size if this is the same as the largest group size,
            # otherwise do nothing
            digit_sum_group_size = digit_sum_group_sizes[digit_sum]

            if digit_sum_group_size > largest_group_size:
                largest_group_size = digit_sum_group_size
                count_with_largest_size = 1
            elif digit_sum_group_size == largest_group_size:
                count_with_largest_size += 1

        return count_with_largest_size


# @leet end
