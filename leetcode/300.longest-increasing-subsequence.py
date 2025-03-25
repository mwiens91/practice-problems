# @leet start
class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        # We'll find, for any given length subsequence, the minimum
        # ending number that subsequence can end with, storing this
        # number in a 0-indexed list where the value at index i is the
        # minimum ending number for a subsequence of length i + 1. For
        # each number, we do a binary search on the minimum ending
        # numbers list to find the insertion index of the number (from 0
        # to the length of the list), then either replace insertion
        # index value with the number or, if the insertion index is the
        # length of the list, append the number.
        minimum_ending_numbers = []

        for num in nums:
            min_ending_nums_len = len(minimum_ending_numbers)

            left = 0
            right = min_ending_nums_len - 1

            while left <= right:
                mid = (left + right) // 2

                if minimum_ending_numbers[mid] < num:
                    left = mid + 1
                else:
                    right = mid - 1

            if left == min_ending_nums_len:
                minimum_ending_numbers.append(num)
            else:
                minimum_ending_numbers[left] = num

        return len(minimum_ending_numbers)


# @leet end
