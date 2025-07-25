# @leet start
class Solution:
    def maxSum(self, nums: list[int]) -> int:
        # For each digit x, store the two largest numbers that have x as
        # their largest digit. Each outer list index i corresponds to
        # the digit i + 1. Each inner list will be in descending
        # order.
        largest_nums_for_digit = [[0, 0] for _ in range(9)]

        for num in nums:
            # Get the largest digit of num
            remaining_num = num
            largest_digit = 0

            while remaining_num:
                largest_digit = max(largest_digit, remaining_num % 10)
                remaining_num //= 10

            # Update the largest numbers of this digit
            largest_nums_list = largest_nums_for_digit[largest_digit - 1]

            if num > largest_nums_list[0]:
                largest_nums_list[1] = largest_nums_list[0]
                largest_nums_list[0] = num
            elif num > largest_nums_list[1]:
                largest_nums_list[1] = num

        # Return the maximum of the sum of largest nums for each digit
        # that is the largest digit for at least two nums
        return max(
            (
                sum(largest_nums_list)
                for largest_nums_list in largest_nums_for_digit
                if largest_nums_list[1] != 0
            ),
            default=-1,
        )


# @leet end
