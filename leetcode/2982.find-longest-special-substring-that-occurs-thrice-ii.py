# @leet start
from string import ascii_lowercase


class Solution:
    def maximumLength(self, s: str) -> int:
        # We'll iterate through s and for each maximal length substring
        # of consecutive characters, keep count of each substring seen
        # that starts with the first index of the maximal length
        # substring. So, for example, a maximal length substring 'aaa'
        # would result in
        #
        # 'a' count incremented once,
        # 'aa' count incremented once,
        # 'aaa' count incremented once.
        #
        # We store the counts in a dictionary with characters as keys
        # and lists as values, where each list index i corresponds to
        # the count of i + 1 length substrings seen.
        counts = {char: [] for char in ascii_lowercase}

        def add_count(char: str, substr_len: int) -> None:
            """Add to the substring count of a character with a given length.

            This function assumes that if we add substring of length N,
            for N > 1, then we've already added a substring with the
            same character of length N - 1.
            """
            if len(counts[char]) >= substr_len:
                # We've already counted a substring of this length for
                # this character, so add to it
                counts[char][substr_len - 1] += 1
            else:
                # This is the first time we've encountered a substring
                # of this length for this character
                counts[char].append(1)

        current_char = s[0]
        current_substring_length = 0

        for char in s:
            # Continue the current substring or start a new one
            if char == current_char:
                current_substring_length += 1
            else:
                current_char = char
                current_substring_length = 1

            # Add to the count
            add_count(current_char, current_substring_length)

        # Find the longest special substringthat occurs at least three
        # times
        best_substring_length = -1

        for char in ascii_lowercase:
            # Go through each substring length from largest to smallest.
            # For a given substring length of size N, we add the count
            # C_N of substrings of length N to the count of substrings
            # of length N - 1, since there are C_N additional substrings
            # of length N - 1 not accounted for in the loop above. (We
            # didn't count them in the loop above for efficiency. Also,
            # I won't prove this assertion here, but it's really easy to
            # convince yourself of if you write out an example.)
            for i in range(len(counts[char]) - 1, -1, -1):
                try:
                    counts[char][i] += counts[char][i + 1]
                except IndexError:
                    pass

                if counts[char][i] >= 3:
                    best_substring_length = max(best_substring_length, i + 1)

                    break

        return best_substring_length


# @leet end
