# @leet start
class Solution:
    def wiggleMaxLength(self, nums: list[int]) -> int:
        # We'll define a general function to find the maximum
        # subsequence using a greedy approach, given whether we want the
        # first difference to be positive or negative.
        def get_max_subsequence(next_diff_positive: bool) -> int:
            prev_num = nums[0]
            subsequence_length = 1

            for current_num in nums[1:]:
                if (
                    next_diff_positive
                    and current_num > prev_num
                    or not next_diff_positive
                    and current_num < prev_num
                ):
                    # Found a difference in the correct direction,
                    # increase subsequence length and change orientation
                    # of difference
                    subsequence_length += 1
                    prev_num = current_num

                    next_diff_positive = not next_diff_positive
                else:
                    # Set previous number to the lowest possible
                    # value if next difference is positive, otherwise
                    # highest possible value
                    if next_diff_positive:
                        prev_num = min(prev_num, current_num)
                    else:
                        prev_num = max(prev_num, current_num)

            return subsequence_length

        return max(get_max_subsequence(True), get_max_subsequence(False))


# @leet end
