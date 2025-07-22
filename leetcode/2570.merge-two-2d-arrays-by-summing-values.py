# @leet start
class Solution:
    def mergeArrays(
        self, nums1: list[list[int]], nums2: list[list[int]]
    ) -> list[list[int]]:
        result: list[list[int]] = []

        n1 = len(nums1)
        n2 = len(nums2)
        i1 = 0
        i2 = 0

        while i1 < n1 and i2 < n2:
            id1 = nums1[i1][0]
            id2 = nums2[i2][0]

            if id1 == id2:
                result.append([id1, nums1[i1][1] + nums2[i2][1]])

                i1 += 1
                i2 += 1
            elif id1 < id2:
                result.append(nums1[i1])

                i1 += 1
            else:
                result.append(nums2[i2])

                i2 += 1

        # At least one of the nums arrays is exhausted
        if i1 < n1:
            result.extend(nums1[i1:])

        if i2 < n2:
            result.extend(nums2[i2:])

        return result


# @leet end
