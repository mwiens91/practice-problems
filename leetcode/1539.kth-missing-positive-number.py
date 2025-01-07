# @leet start
class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
        # If the first element x of the array has k or more missing
        # numbers preceding it (i.e., x > k), then the kth missing
        # number is k
        if arr[0] > k:
            return k

        # The number of missing numbers occuring prior to a given
        # element x with index i is equal to x - (i + 1).
        def get_num_preceding_missing_nums(idx: int) -> int:
            return arr[idx] - idx - 1

        # Do a binary search to find the rightmost element x that has
        # less than or equal to k - 1 preceding missing numbers such
        # that x is the final element of the array or the next element
        # has more than or equal to k missing numbers. Once we find this
        # element, the kth missing number will be given by x + k - k',
        # where k' is the number of missing numbers preceding x
        n = len(arr)

        left = 0
        right = n - 1

        while True:
            mid = (left + right) // 2
            number_missing_nums_before_mid = get_num_preceding_missing_nums(mid)

            if number_missing_nums_before_mid <= k - 1 and (
                mid == n - 1 or get_num_preceding_missing_nums(mid + 1) >= k
            ):
                return arr[mid] + k - number_missing_nums_before_mid

            if number_missing_nums_before_mid <= k - 1:
                left = mid + 1
            elif number_missing_nums_before_mid > k - 1:
                right = mid - 1


# @leet end
