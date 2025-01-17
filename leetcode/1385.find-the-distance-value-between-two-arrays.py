# @leet start
class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        # The question working is not as clear as it could be. For each
        # element x of arr1, if for all elements y of arr2, |x - y| > d
        # then x increases the distance value of arr1. So what we can do
        # for this is do a binary search using each element x of arr1
        # looking for any element y such that |x - y| <= d: if we find
        # such a y, x does not contribute to the distance value;
        # otherwise it does.

        # First sort arr2 so we can actually do a binary search on it
        arr2.sort()

        # Now do a binary search on arr2 using each element x of arr1
        distance_value = 0

        arr2_length = len(arr2)

        for x in arr1:
            left = 0
            right = arr2_length - 1

            contributes_to_distance_value = True

            while left <= right:
                mid = (left + right) // 2
                y = arr2[mid]

                if abs(x - y) <= d:
                    contributes_to_distance_value = False

                    break

                if y < x:
                    left = mid + 1
                else:
                    # x < y
                    right = mid - 1

            if contributes_to_distance_value:
                distance_value += 1

        return distance_value


# @leet end
