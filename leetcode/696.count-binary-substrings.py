# @leet start
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        # Count the run lengths of consecutive bit values in order
        run_lengths: list[int] = []

        current_bit = s[0]
        num_consecutive = 0

        for bit in s:
            if bit == current_bit:
                num_consecutive += 1
            else:
                run_lengths.append(num_consecutive)

                current_bit = bit
                num_consecutive = 1

        # Count final run length
        run_lengths.append(num_consecutive)

        # For each consecutive pair of run lengths, the number of valid
        # binary substrings that can be formed is equal to the minimum
        # of the run lengths
        num_valid_substrings = 0

        for run_len_1, run_len_2 in zip(run_lengths, run_lengths[1:]):
            num_valid_substrings += min(run_len_1, run_len_2)

        return num_valid_substrings


# @leet end
