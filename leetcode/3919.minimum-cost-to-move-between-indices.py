# @leet start
class Solution:
    def minCost(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        n = len(nums)
        prefix_costs = [0] * n
        prefix_costs[1] = 1

        for i in range(2, n):
            if nums[i] - nums[i - 1] < nums[i - 1] - nums[i - 2]:
                prefix_costs[i] = 1 + prefix_costs[i - 1]
            else:
                prefix_costs[i] = nums[i] - nums[i - 1] + prefix_costs[i - 1]

        suffix_costs = [0] * n
        suffix_costs[n - 2] = 1

        for i in range(n - 3, -1, -1):
            if nums[i + 1] - nums[i] <= nums[i + 2] - nums[i + 1]:
                suffix_costs[i] = 1 + suffix_costs[i + 1]
            else:
                suffix_costs[i] = nums[i + 1] - nums[i] + suffix_costs[i + 1]

        res: list[int] = []

        for start, end in queries:
            if start < end:
                res.append(prefix_costs[end] - prefix_costs[start])
            else:
                res.append(suffix_costs[end] - suffix_costs[start])

        return res


# @leet end
