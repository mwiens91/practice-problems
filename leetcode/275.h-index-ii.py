# @leet start
class Solution:
    def hIndex(self, citations: list[int]) -> int:
        n = len(citations)

        left = 0
        right = n - 1

        # Find last index where #citations <= #papers to right
        while left <= right:
            mid = (left + right) // 2

            n_suffix = n - mid

            if citations[mid] == n_suffix:
                return n_suffix

            if citations[mid] <= n_suffix:
                left = mid + 1
            else:
                right = mid - 1

        if right < 0:
            return n - right - 1

        return max(citations[right], n - right - 1)


# @leet end
