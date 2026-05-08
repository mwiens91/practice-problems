# @leet start
class Solution:
    def equationsPossible(self, equations: list[str]) -> bool:
        CODE_POINT_A = ord("a")
        N = 26
        parent = list(range(N))
        size = [1] * N

        def find(a: int) -> int:
            if a != parent[a]:
                parent[a] = find(parent[a])

            return parent[a]

        def union(a: int, b: int) -> None:
            p_a = find(a)
            p_b = find(b)

            if p_a == p_b:
                return

            if size[p_a] < size[p_b]:
                p_a, p_b = p_b, p_a

            parent[p_b] = p_a
            size[p_a] += size[p_b]

        not_equal: list[tuple[int, int]] = []

        for s_a, eq, _, s_b in equations:
            a = ord(s_a) - CODE_POINT_A
            b = ord(s_b) - CODE_POINT_A

            if eq == "=":
                union(a, b)
            else:
                not_equal.append((a, b))

        for a, b in not_equal:
            if find(a) == find(b):
                return False

        return True


# @leet end
