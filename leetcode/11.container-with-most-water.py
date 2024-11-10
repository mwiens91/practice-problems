# @leet start
class Solution:
    def maxArea(self, height: list[int]) -> int:
        # We'll use a forwards and backwards iterator to compute
        # candidates for the best area
        i = 0
        j = len(height) - 1

        best = 0

        while i < j:
            best = max(best, (j - i) * min(height[i], height[j]))

            # Move the iterator which points to a shorter height. The
            # larger height can potentially hold more water so we want
            # to keep it.
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1

        return best


# @leet end
