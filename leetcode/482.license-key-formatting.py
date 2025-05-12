# @leet start
class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        # Put all characters in a list as uppercase
        key_chars = [char.upper() for char in s if char != "-"]

        # Insert dashes
        dash_insert_countdown = len(key_chars) % k or k
        result_chars: list[str] = []

        for char in key_chars:
            if dash_insert_countdown == 0:
                result_chars.append("-")

                dash_insert_countdown = k - 1
            else:
                dash_insert_countdown -= 1

            result_chars.append(char)

        return "".join(result_chars)


# @leet end
