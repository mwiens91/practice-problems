# @leet start
from math import inf


class Solution:
    def distributeCookies(self, cookies: list[int], k: int) -> int:
        best: int | float = inf
        dist = [0] * k

        def backtrack(idx: int) -> None:
            nonlocal best

            if idx == len(cookies):
                best = min(best, max(dist))

                return

            seen: set[int] = set()

            for i in range(k):
                if dist[i] in seen:
                    continue

                seen.add(dist[i])

                dist[i] += cookies[idx]
                backtrack(idx + 1)
                dist[i] -= cookies[idx]

        backtrack(0)

        return best


# @leet end
