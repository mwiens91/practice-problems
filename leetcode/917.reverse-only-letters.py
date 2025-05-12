# @leet start
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        char_list = list(s)
        alpha_chars = [char for char in char_list if char.isalpha()]

        # Replace the characters in char_list in reverse order
        alpha_char_idx = len(alpha_chars) - 1

        for i, char in enumerate(char_list):
            if char.isalpha():
                char_list[i] = alpha_chars[alpha_char_idx]
                alpha_char_idx -= 1

        return "".join(char_list)


# @leet end
