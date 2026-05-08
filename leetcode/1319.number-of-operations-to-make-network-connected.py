# @leet start
class Solution:
    def makeConnected(self, n: int, connections: list[list[int]]) -> int:
        parent = list(range(n))
        size = [1] * n
        extra = 0

        def find(a: int) -> int:
            if a != parent[a]:
                parent[a] = find(parent[a])

            return parent[a]

        def union(a: int, b: int) -> None:
            nonlocal extra

            p_a = find(a)
            p_b = find(b)

            if p_a == p_b:
                extra += 1
                return

            if size[p_a] < size[p_b]:
                p_a, p_b = p_b, p_a

            parent[p_b] = p_a
            size[p_a] += p_b

        for a, b in connections:
            union(a, b)

        # Connected components - 1
        needed = sum(parent[i] == i for i in range(n)) - 1

        return needed if needed <= extra else -1


# @leet end
