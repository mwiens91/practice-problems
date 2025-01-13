# @leet start
class Solution:
    def minimumLevels(self, possible: list[int]) -> int:
        # Get cumulative sums from the left and right, treating 1 as 1
        # and 0 as -1
        n = len(possible)

        def get_cumulative_sums(forward: bool) -> list[int]:
            range_ = range(n) if forward else range(n - 1, -1, -1)

            result = [0] * n
            current_total = 0

            for i in range_:
                current_val = 1 if possible[i] == 1 else -1
                current_total += current_val

                result[i] = current_total

            return result

        left_cumulative_sums = get_cumulative_sums(True)
        right_cumulative_sums = get_cumulative_sums(False)

        # We want to find the smallest index i such that Alice plays
        # levels 0 -> i and Bob plays games i + 1 -> n - 1 and Alice has
        # more points than Bob. If this index exists, return it +1,
        # since the answer needs to be 1-indexed.
        for i in range(n - 1):
            if left_cumulative_sums[i] > right_cumulative_sums[i + 1]:
                return i + 1

        # Not possible for Alice to win
        return -1


# @leet end
