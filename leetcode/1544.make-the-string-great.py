# @leet start
class Solution:
    def makeGood(self, s: str) -> str:
        def get_char_complement(char: str) -> str:
            return char.upper() if char.islower() else char.lower()

        result_chars_stack: list[str] = []

        for char in s:
            if (
                result_chars_stack
                and get_char_complement(result_chars_stack[-1]) == char
            ):
                # Remove complement character from the stack and discard
                # this character
                result_chars_stack.pop()
            else:
                # Add this character to the stack
                result_chars_stack.append(char)

        return "".join(result_chars_stack)


# @leet end
