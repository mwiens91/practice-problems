# @leet start
class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # In order to run in O(m + n) time complexity, we use a
        # temporary array to store results, and then copy the elements
        # from that array into num1. Here i will traverse nums1, j will
        # traverse nums2
        i = 0
        j = 0

        # NOTE: it'd be faster to initialize this with [0] * (m + n) and
        # then index below, but I'm not going to bother with that right
        # now
        temp = []

        # Exhaust one of the arrays
        while i < m and j < n:
            if (num1 := nums1[i]) <= (num2 := nums2[j]):
                temp.append(num1)
                i += 1
            else:
                temp.append(num2)
                j += 1

        # Put the rest of the remaining array into temp
        if i == m:
            while j < n:
                temp.append(nums2[j])
                j += 1
        else:
            while i < m:
                temp.append(nums1[i])
                i += 1

        # Copy elements into nums1
        for i, num in enumerate(temp):
            nums1[i] = num


# @leet end
