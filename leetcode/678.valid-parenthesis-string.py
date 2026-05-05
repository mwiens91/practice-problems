# @leet start
class Solution:
    def checkValidString(self, s: str) -> bool:
        open: list[int] = []
        wildcard: list[int] = []

        for i, ch in enumerate(s):
            if ch == "(":
                open.append(i)
            elif ch == "*":
                wildcard.append(i)
            else:
                if open:
                    open.pop()
                elif wildcard:
                    wildcard.pop()
                else:
                    return False

        while open and wildcard and open[-1] < wildcard[-1]:
            open.pop()
            wildcard.pop()

        return len(open) == 0


# @leet end
