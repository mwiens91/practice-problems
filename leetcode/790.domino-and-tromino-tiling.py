# @leet start
class Solution:
    def numTilings(self, n: int) -> int:
        MOD = int(1e9 + 7)

        empty_at_next = 1
        full_at_next = 0
        one_gap_at_next = 0

        for _ in range(n):
            empty_at_next, full_at_next, one_gap_at_next = (
                (empty_at_next + full_at_next) % MOD,
                (empty_at_next + one_gap_at_next) % MOD,
                (2 * empty_at_next + one_gap_at_next) % MOD,
            )

        return empty_at_next


# @leet end
