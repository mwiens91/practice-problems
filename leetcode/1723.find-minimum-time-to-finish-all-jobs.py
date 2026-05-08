# @leet start
class Solution:
    def minimumTimeRequired(self, jobs: list[int], k: int) -> int:
        jobs.sort(reverse=True)
        best: int = sum(jobs[: len(jobs) // k + 1])
        dist = [0] * k

        def backtrack(idx: int) -> None:
            nonlocal best

            if idx == len(jobs):
                best = min(best, max(dist))

                return

            if max(dist) >= best:
                return

            seen: set[int] = set()

            for i in range(k):
                if dist[i] in seen:
                    continue

                seen.add(dist[i])

                dist[i] += jobs[idx]
                backtrack(idx + 1)
                dist[i] -= jobs[idx]

        backtrack(0)

        return best


# @leet end
