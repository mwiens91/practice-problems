# @leet start
class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        SPECIAL_CHARS = {"!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "+"}

        # Check length is sufficient
        if len(password) < 8:
            return False

        # Check other conditions
        prev_char = ""

        has_lower = False
        has_upper = False
        has_digit = False
        has_special = False

        for char in password:
            if char == prev_char:
                return False

            if char.islower():
                has_lower = True
            elif char.isupper():
                has_upper = True
            elif char.isdigit():
                has_digit = True
            elif char in SPECIAL_CHARS:
                has_special = True

            prev_char = char

        return has_lower and has_upper and has_digit and has_special


# @leet end
