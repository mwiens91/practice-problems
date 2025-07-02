# @leet start
from string import ascii_lowercase


class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        decode_dict = {" ": " "}
        letters = iter(ascii_lowercase)

        for char in key:
            if char not in decode_dict:
                decode_dict[char] = next(letters)

        return "".join(decode_dict[char] for char in message)


# @leet end
