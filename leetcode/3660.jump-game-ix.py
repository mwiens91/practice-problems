# @leet start
class Solution:
    def maxValue(self, nums: list[int]) -> list[int]:
        n = len(nums)
        parent = list(range(n))
        size = [1] * n

        def find(a: int) -> int:
            if a != parent[a]:
                parent[a] = parent[parent[a]]

            return parent[a]

        def union(a: int, b: int) -> None:
            lead_a = find(a)
            lead_b = find(b)

            if lead_a != lead_b:
                # Invariant: lead_a larger
                if size[lead_a] < size[lead_b]:
                    lead_a, lead_b = lead_b, lead_a

                parent[lead_b] = lead_a
                size[lead_a] += size[lead_b]

        stack: list[int] = []

        for i in range(n):
            leader = stack[-1] if stack and nums[stack[-1]] > nums[i] else i

            while stack and nums[stack[-1]] > nums[i]:
                union(stack.pop(), i)

            stack.append(leader)

        for i in range(n):
            p = find(i)
            nums[p] = max(nums[p], nums[i])

        return [nums[find(i)] for i in range(n)]


# @leet end
