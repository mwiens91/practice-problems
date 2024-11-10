# @leet start
class Solution:
    def romanToInt(self, s: str) -> int:
        # Useful data for numerals: their order and their values
        numeral_order = [
            "M",
            "CM",
            "D",
            "CD",
            "C",
            "XC",
            "L",
            "XL",
            "X",
            "IX",
            "V",
            "IV",
            "I",
        ]
        numeral_values = {
            "M": 1000,
            "CM": 900,
            "D": 500,
            "CD": 400,
            "C": 100,
            "XC": 90,
            "L": 50,
            "XL": 40,
            "X": 10,
            "IX": 9,
            "V": 5,
            "IV": 4,
            "I": 1,
        }

        # Get the length of the string
        n = len(s)

        # Find the value of the passed in string, try using each numeral
        # in the list above until the string is exhausted
        res = 0
        i = 0

        for numeral in numeral_order:
            numeral_length = len(numeral)

            while i + numeral_length <= n and s[i : i + numeral_length] == numeral:
                res += numeral_values[numeral]
                i += numeral_length

                # Since there is always a solution, this condition will
                # eventually return True
                if i == n:
                    return res


# @leet end
