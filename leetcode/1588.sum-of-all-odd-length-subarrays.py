# @leet start
class Solution:
    def sumOddLengthSubarrays(self, arr: list[int]) -> int:
        n = len(arr)

        sum_odd_length_subarrays = 0

        for i, num in enumerate(arr):
            # Count the number of odd-length subarrays the number is
            # a part of. For any subarray, there are i + 1 choices for
            # the starting index and there are n - i choices for the
            # ending index. The total number of subarrays is thus given
            # by (i + 1) * (n - i).
            #
            # I won't justify the following here because I don't know
            # how to; however, if you take out pencil and paper and look
            # at a few examples it will be easy to convince yourself of
            # this. Let T be the total number of subarrays a given
            # element is a member of. If T is even, there are exactly
            # T / 2 even and odd-length subarrays. If T is odd, however,
            # there are T // 2 even-length subarrays and T // 2 + 1
            # odd-length subarrays; i.e., there is one additional odd
            # subarray and the rest are split evenly.
            count = ((i + 1) * (n - i) + 1) // 2

            # Add this number to the sum for each odd-length subarray
            # the number is a part of
            sum_odd_length_subarrays += num * count

        return sum_odd_length_subarrays



# @leet end
