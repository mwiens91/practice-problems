# @leet start
class Solution:
    def reverseParentheses(self, s: str) -> str:
        res: list[str] = []
        start_idx_stack: list[int] = []

        def swap(start: int, delta: int):
            for i in range(delta):
                res[start + i], res[len(res) - 1 - i] = (
                    res[len(res) - 1 - i],
                    res[start + i],
                )

        for ch in s:
            if ch == "(":
                # Push index of the next char we'll push to res
                start_idx_stack.append(len(res))
            elif ch == ")":
                start = start_idx_stack.pop()
                swap(start, (len(res) - start) // 2)
            else:
                res.append(ch)

        return "".join(res)


# @leet end
