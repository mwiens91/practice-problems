# @leet start
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        # Keep all possible combinations in here
        generated = []

        # Recursively find all combinations
        def generate_recurse(n_left: int, n_unclosed: int = 0, str_: str = "") -> None:
            """
            n_unclosed: number of unclosed left parentheses
            n_left: number of left parantheses we need to put in
            """
            # Base case
            if n_unclosed == 0 and n_left == 0:
                generated.append(str_)
                return

            if n_unclosed:
                # Close a parenthesis
                generate_recurse(n_left, n_unclosed - 1, str_ + ")")

            if n_left:
                # Start new unclosed parenthesis
                generate_recurse(n_left - 1, n_unclosed + 1, str_ + "(")

            return

        generate_recurse(n)

        return generated


# @leet end
