# @leet start
class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        LETTERS = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        res: list[str] = []
        curr: list[str] = []

        def backtrack(i: int) -> None:
            if i == len(digits):
                res.append("".join(curr))

                return

            for ch in LETTERS[digits[i]]:
                curr.append(ch)
                backtrack(i + 1)
                curr.pop()

            return

        backtrack(0)

        return res


# @leet end
