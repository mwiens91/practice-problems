# @leet start
class Solution:
    def letterCasePermutation(self, s: str) -> list[str]:
        result: list[list[str]] = [[]]

        for char in s:
            if char.isdigit():
                for l in result:
                    l.append(char)
            else:
                result_copy = [l[:] for l in result]

                lower_char = char.lower()
                upper_char = char.upper()

                for i in range(len(result)):  # pylint: disable=consider-using-enumerate
                    result[i].append(lower_char)
                    result_copy[i].append(upper_char)

                result = result + result_copy

        return ["".join(l) for l in result]


# @leet end
