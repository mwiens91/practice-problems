# @leet start
from string import ascii_lowercase


class Solution:
    def modifyString(self, s: str) -> str:
        # Replace all ?s with a character that isn't the previous or
        # next character
        chars_list = list(s)

        n = len(chars_list)

        for i, char in enumerate(chars_list):
            if char == "?":
                # Get next and previous characters
                exclude_set: set[str] = set()

                if i > 0:
                    exclude_set.add(chars_list[i - 1])

                if i < n - 1:
                    exclude_set.add(chars_list[i + 1])

                # Replace the ? with something not in the exclude set
                for letter in ascii_lowercase:
                    if letter not in exclude_set:
                        chars_list[i] = letter

                        break

        return "".join(chars_list)


# @leet end
