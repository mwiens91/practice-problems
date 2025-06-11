# @leet start
class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        def get_string_value(s: str) -> int:
            val = 0

            # Sum each letter value multiplied by 10 to the power of its
            # index from the right
            for exponent, char in enumerate(reversed(s)):
                val += (ord(char) - ord("a")) * 10**exponent

            return val

        return get_string_value(firstWord) + get_string_value(
            secondWord
        ) == get_string_value(targetWord)


# @leet end
