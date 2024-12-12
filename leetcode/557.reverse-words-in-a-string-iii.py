# @leet start
class Solution:
    def reverseWords(self, s: str) -> str:
        # Since strings are immutable in Python, we'll work with a list
        # of characters and turn it back into a string when we're done
        chars = list(s)
        n = len(chars)

        # Define function to reverse a word in a list
        def reverse_word(left: int, right: int) -> None:
            while left < right:
                chars[left], chars[right] = chars[right], chars[left]

                left += 1
                right -= 1

        # Our algorithm will work as follows. We start with a left
        # pointer i pointing to the beginning of a word. We move a right
        # pointer j to the end of the word. We then reverse the word.
        # Then we move i to the next word if there is another word.
        i = 0

        while i < n:
            # Move right pointer to end of word
            j = i

            while j < n - 1 and chars[j + 1] != " ":
                j += 1

            # Swap chars
            reverse_word(i, j)

            # Move left to next word
            i = j + 2

        return "".join(chars)


# @leet end
