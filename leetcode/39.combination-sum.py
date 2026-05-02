# @leet start
class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()

        res: list[list[int]] = []
        curr: list[int] = []

        def backtrack(i: int, accum: int) -> None:
            """i is candidate index, accum is sum of curr."""
            if accum == target:
                res.append(curr[:])
                return

            for j in range(i, len(candidates)):
                new_accum = accum + candidates[j]

                # Early return optimization
                if new_accum > target:
                    break

                curr.append(candidates[j])
                backtrack(j, new_accum)
                curr.pop()

        backtrack(0, 0)

        return res


# @leet end
