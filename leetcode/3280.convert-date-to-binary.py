# @leet start
class Solution:
    def convertDateToBinary(self, date: str) -> str:
        def int_string_to_binary_string(int_str: str) -> str:
            return bin(int(int_str))[2:]

        return "-".join(int_string_to_binary_string(x) for x in date.split(sep="-"))


# @leet end
