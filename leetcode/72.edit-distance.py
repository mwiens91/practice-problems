# @leet start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # Memo: minimum number of operations to turn the first element
        # of the tuple key into the second element
        memo: dict[tuple(str, str), int] = {("", ""): 0}

        # Function to find number of changes to convert s1 into s2
        def num_changes(s1: str, s2: str) -> int:
            # Return the result if we've done this before
            if (s1, s2) in memo:
                return memo[(s1, s2)]

            # Calculate number of changes
            changes = 0

            if not s1:
                # We need to insert the remaining characters in s2
                changes = len(s2)
            elif not s2:
                # We need to remove the remaining characters in s1
                changes = len(s1)
            elif s1[0] == s2[0]:
                # If the first two characters are the same, try again
                # with those characters stripped
                changes = num_changes(s1[1:], s2[1:])
            else:
                # Try each of inserting the character, removing a
                # character, and replacing a character
                changes = 1 + min(
                    num_changes(s1, s2[1:]),  # insert
                    num_changes(s1[1:], s2),  # remove
                    num_changes(s1[1:], s2[1:]),  # replace
                )

            # Memoize
            memo[(s1, s2)] = changes

            return changes

        return num_changes(word1, word2)


# @leet end
