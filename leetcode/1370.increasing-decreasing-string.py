# @leet start
from collections import Counter


class Solution:
    def sortString(self, s: str) -> str:
        freqs = Counter(s)
        sorted_chars_asc = sorted(freqs)
        sorted_chars_desc = sorted_chars_asc[::-1]

        result: list[str] = []
        done = False

        while not done:
            done = True

            for char_list in [sorted_chars_asc, sorted_chars_desc]:
                for char in char_list:
                    if freqs[char] > 0:
                        result.append(char)
                        freqs[char] -= 1
                        done = False

        return "".join(result)


# @leet end
