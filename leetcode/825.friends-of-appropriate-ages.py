# @leet start
class Solution:
    def numFriendRequests(self, ages: list[int]) -> int:
        n = len(ages)
        ages.sort()

        res = 0
        left = 0

        i = 0

        while i < n:
            mult = 1

            while i < n - 1 and ages[i] == ages[i + 1]:
                i += 1
                mult += 1

            target = ages[i] / 2 + 7
            right = i - 1

            while left <= right:
                mid = (left + right) // 2

                if ages[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1

            res += mult * (i - left)
            i += 1

        return res


# @leet end
