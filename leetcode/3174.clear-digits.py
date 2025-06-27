# @leet start
class Solution:
    def clearDigits(self, s: str) -> str:
        letter_stack: list[str] = []

        for char in s:
            if char.isdigit():
                if letter_stack:
                    letter_stack.pop()
            else:
                letter_stack.append(char)

        return "".join(letter_stack)


# @leet end
