# @leet start
import re


class Solution:
    def freqAlphabets(self, s: str) -> str:
        nums_in_s = (int(m.rstrip("#")) for m in re.findall(r"\d{2}#|\d", s))

        decoded_chars_in_s: list[str] = []
        a_code_point = ord("a")

        for num in nums_in_s:
            decoded_chars_in_s.append(chr(a_code_point + num - 1))

        return "".join(decoded_chars_in_s)


# @leet end
