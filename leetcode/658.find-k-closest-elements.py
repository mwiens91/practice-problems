# @leet start
class Solution:
    def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
        # NOTE: there's a O(log(n - k) + k) time solution that I haven't
        # implemented. This is just O(log(n) + k) time.
        n = len(arr)

        # Find the first number greater than or equal to x
        left = 0
        right = n - 1

        while left <= right:
            mid = (left + right) // 2

            if arr[mid] < x:
                left = mid + 1
            else:
                right = mid - 1

        # Get the k closest elements to x from arr
        if left == n:
            return arr[-k:]

        if left == 0:
            return arr[:k]

        # k_left and k_right are the inclusive indices of the k-length
        # subinterval in arr that contain the integers closest to x
        k_left = left - 1 if x - arr[left - 1] <= arr[left] - x else left
        k_right = k_left

        while k_right - k_left + 1 < k:
            if k_left == 0:
                k_right = k - 1
            elif k_right == n - 1:
                k_left = n - k
            elif abs(x - arr[k_left - 1]) <= abs(x - arr[k_right + 1]):
                k_left -= 1
            else:
                k_right += 1

        return arr[k_left : k_right + 1]


# @leet end
