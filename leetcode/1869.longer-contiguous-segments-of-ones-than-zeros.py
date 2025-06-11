# @leet start
class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        longest_run_lengths = {"0": 0, "1": 0}

        current_run_length = 0
        current_run_char = s[0]

        for char in s:
            # Add to current run if same char else update max run length
            # and start new run
            if char == current_run_char:
                current_run_length += 1
            else:
                # Update max
                longest_run_lengths[current_run_char] = max(
                    longest_run_lengths[current_run_char], current_run_length
                )

                # Start new run
                current_run_length = 1
                current_run_char = char

        # Update max for the final run
        longest_run_lengths[current_run_char] = max(
            longest_run_lengths[current_run_char], current_run_length
        )

        return longest_run_lengths["1"] > longest_run_lengths["0"]


# @leet end
