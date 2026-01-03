# @leet start
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        OPEN_PAREN = "("

        # Get the inner part of each primative string in the
        # decomposition of s
        results: list[str] = []

        def add_to_results(start_idx: int, end_idx: int) -> None:
            if start_idx - end_idx > 2:
                results.append(s[start_idx + 1 : end_idx])

        n = len(s)
        part_start_idx = 0
        num_unclosed = 1

        for i in range(1, n):
            # If there are no unclosed parentheses, we've just finished
            # a part, so process it and set up for the next part
            if num_unclosed == 0:
                add_to_results(part_start_idx, i - 1)
                part_start_idx = i

            # Process current part
            if s[i] == OPEN_PAREN:
                num_unclosed += 1
            else:
                num_unclosed -= 1

        # Add last part to results
        add_to_results(part_start_idx, n - 1)

        return "".join(results)


# @leet end
