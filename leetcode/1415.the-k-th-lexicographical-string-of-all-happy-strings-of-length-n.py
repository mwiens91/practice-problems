# @leet start
class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        if k > 3 * 2 ** (n - 1):
            # there aren't k happy strings of this length
            return ""

        curr: list[str] = []
        count = 0

        def backtrack(i: int) -> None:
            nonlocal count

            if i == n:
                count += 1

                return

            for ch in ("a", "b", "c"):
                if not curr or ch != curr[-1]:
                    curr.append(ch)

                    backtrack(i + 1)

                    if count == k:
                        return

                    curr.pop()

        backtrack(0)

        return "".join(curr)


# @leet end
