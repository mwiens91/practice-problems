# @leet start
class Solution:
    def predictTheWinner(self, nums: list[int]) -> bool:
        # Define a memoized, recursive function to find the score
        # difference between player 1 and 2 given a starting index of
        # and ending index (inclusive) of nums
        n = len(nums)

        score_differences: list[list[None | int]] = [[None] * n for _ in range(n)]

        def find_score_difference(start_idx: int, end_idx: int) -> int:
            # If start index is greater than end index we've exhausted
            # nums and we're done
            if start_idx > end_idx:
                return 0

            # If start index is the same as end index, our score is the
            # single number
            if start_idx == end_idx:
                return nums[start_idx]

            # Try to use a memoized result
            if (score_difference := score_differences[start_idx][end_idx]) is not None:
                return score_difference

            # Calculate the optimal score difference based on the four
            # different ways this round can go
            score_difference = max(
                min(
                    find_score_difference(start_idx + 2, end_idx)
                    + nums[start_idx]
                    - nums[start_idx + 1],
                    find_score_difference(start_idx + 1, end_idx - 1)
                    + nums[start_idx]
                    - nums[end_idx],
                ),
                min(
                    find_score_difference(start_idx, end_idx - 2)
                    + nums[end_idx]
                    - nums[end_idx - 1],
                    find_score_difference(start_idx + 1, end_idx - 1)
                    + nums[end_idx]
                    - nums[start_idx],
                ),
            )

            # Memoize and return the result
            score_differences[start_idx][end_idx] = score_difference

            return score_difference

        return find_score_difference(0, n - 1) >= 0


# @leet end
