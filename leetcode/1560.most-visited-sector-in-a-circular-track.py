# @leet start
class Solution:
    def mostVisited(self, n: int, rounds: list[int]) -> list[int]:
        # If we treat this problem as 0-indexed (it's 1-indexed), then
        # the most visited elements are obtained by counting from
        # rounds[0] to rounds[-1] modulus n
        first_round = rounds[0]
        last_round = rounds[-1]

        if first_round > last_round:
            return list(range(1, last_round + 1)) + list(range(first_round, n + 1))

        # first_round <= last_round
        return list(range(first_round, last_round + 1))


# @leet end
