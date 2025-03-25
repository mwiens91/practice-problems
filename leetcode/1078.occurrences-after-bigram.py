# @leet start
class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> list[str]:
        # Split the text into words
        words = text.split()
        num_words = len(words)

        # Count the number of third words
        thirds: list[str] = []

        i = 0

        while i < num_words - 2:
            if words[i] == first and words[i + 1] == second:
                thirds.append(words[i + 2])

            i += 1

        return thirds


# @leet end
