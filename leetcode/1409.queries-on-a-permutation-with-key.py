# @leet start
class Solution:
    def processQueries(self, queries: list[int], m: int) -> list[int]:
        res: list[int] = []
        perm = [i for i in range(1, m + 1)]
        pos = [i - 1 for i in range(m + 1)]

        for q in queries:
            res.append(pos[q])

            for i in range(pos[q], 0, -1):
                perm[i] = perm[i - 1]
                pos[perm[i]] = i

            perm[0] = q
            pos[q] = 0

        return res


# @leet end
