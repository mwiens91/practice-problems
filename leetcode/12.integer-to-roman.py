# @leet start
class Solution:
    def intToRoman(self, num: int) -> str:
        VAL_SYMBOL_TUPLES = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I"),
        ]

        result: list[str] = []

        for val, symbol in VAL_SYMBOL_TUPLES:
            while num >= val:
                result.append(symbol)
                num -= val

        return "".join(result)


# @leet end
