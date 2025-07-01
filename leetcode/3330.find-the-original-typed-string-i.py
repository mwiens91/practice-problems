# @leet start
class Solution:
    def possibleStringCount(self, word: str) -> int:
        string_count = 1

        run_length = 0
        prev_char = word[0]

        for char in word:
            if char == prev_char:
                run_length += 1
            else:
                # Update string count
                string_count += run_length - 1

                # Set up for next iteration
                run_length = 1
                prev_char = char

        # Update string count one last time
        string_count += run_length - 1

        return string_count


# @leet end
