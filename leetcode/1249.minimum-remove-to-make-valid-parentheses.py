# @leet start
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        forward: list[str] = []
        open_count = 0

        for ch in s:
            if ch == "(":
                open_count += 1
            elif ch == ")":
                if not open_count:
                    continue

                open_count -= 1

            forward.append(ch)

        backward: list[str] = []

        for ch in reversed(forward):
            if ch == "(" and open_count:
                open_count -= 1
            else:
                backward.append(ch)

        return "".join(reversed(backward))


# @leet end
