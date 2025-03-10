# @leet start
class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        # Use a k length sliding window. Use a counter dictionary to
        # keep track of the counts of letters in the window. The
        # dictionary will only hold keys with positive counts.
        letter_counts = {}

        def increase_count(letter: str) -> None:
            try:
                letter_counts[letter] += 1
            except KeyError:
                letter_counts[letter] = 1

        def decrease_count(letter: str) -> None:
            letter_counts[letter] -= 1

            if letter_counts[letter] == 0:
                del letter_counts[letter]

        # Only count the first k - 1 characters of s here; we'll add the
        # kth character in the loop below
        for letter in s[: k - 1]:
            increase_count(letter)

        # Begin sliding the window
        n = len(s)

        for i in range(k - 1, n):
            # Add next letter to window
            increase_count(s[i])

            # Check if window has exactly one letter
            if len(letter_counts) == 1:
                # It does. Get the letter
                letter = next(iter(letter_counts))

                # Return True if it is different than the previous and
                # next letters
                if (i < k or letter != s[i - k]) and (i == n - 1 or letter != s[i + 1]):
                    return True

            # Set up for next iteration
            decrease_count(s[i - k + 1])

        return False


# @leet end
