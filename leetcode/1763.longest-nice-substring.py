# @leet start
class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        # We're going to test every possible substring starting from the
        # earliest to the latest.
        best_nice_substring = None
        best_nice_substring_length = 0

        n = len(s)

        for start_idx in range(n):
            chars_set = set(s[start_idx])
            num_unmatched = 1

            for idx in range(start_idx + 1, n):
                char = s[idx]

                # If this is a new character, increase or decrease the
                # number of unmatched characters
                if char not in chars_set:
                    if (
                        char.isupper()
                        and char.lower() in chars_set
                        or char.islower()
                        and char.upper() in chars_set
                    ):
                        # Match in set
                        num_unmatched -= 1
                    else:
                        # No match in set
                        num_unmatched += 1

                    # Add char to the set
                    chars_set.add(char)

                # If our substring is nice, update the best nice
                # substring
                if (
                    num_unmatched == 0
                    and (length := idx + 1 - start_idx) > best_nice_substring_length
                ):
                    best_nice_substring = s[start_idx : idx + 1]
                    best_nice_substring_length = length

        return best_nice_substring if best_nice_substring is not None else ""


# @leet end
