# @leet start
import re


class Solution:
    def maskPII(self, s: str) -> str:
        if s[0].isalpha():
            # Email. Convert to lowercase and mask middle characters.
            s = s.lower()

            name, domain = s.split("@")

            return name[0] + "*****" + name[-1] + "@" + domain

        # Phone number. First get all digits.
        digits = re.findall(r"\d", s)

        # Make masked country code
        prefix = ""

        num_digits = len(digits)

        if num_digits > 10:
            prefix = "+" + "*" * (num_digits - 10) + "-"

        # Combine masked country code with masked number
        return prefix + "***-***-" + "".join(digits[-4:])


# @leet end
