# @leet start
class Solution:
    def maxDistance(self, colors: list[int]) -> int:
        # If the houses on either end of the array are different, we use
        # those houses. Otherwise, we fix the left house and find the
        # closest house to the right with a different colour, do the
        # same thing fixing the right house and varying the left house,
        # and choose the best result of those.
        n = len(colors)

        if colors[0] != colors[n - 1]:
            return n - 1

        result_options: list[int] = []

        # Fix left house, vary right
        for i in range(n - 2, 0, -1):
            if colors[0] != colors[i]:
                result_options.append(i)

                break

        # Fix right house, vary left
        for i in range(1, n - 1):
            if colors[i] != colors[n - 1]:
                result_options.append(n - 1 - i)

                break

        return max(result_options)


# @leet end
