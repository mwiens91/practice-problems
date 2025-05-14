# @leet start
import re


class Solution:
    def defangIPaddr(self, address: str) -> str:
        return re.sub(r"\.", r"[.]", address)


# @leet end
