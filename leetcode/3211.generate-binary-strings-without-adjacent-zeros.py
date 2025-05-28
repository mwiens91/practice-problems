# @leet start
class Solution:
    def validStrings(self, n: int) -> list[str]:
        results: list[str] = []

        def generate_strings(current: str, last_char: str = "") -> None:
            # Base case: added final bit
            if len(current) == n:
                results.append(current)

                return

            # Recurse
            generate_strings(current + "1", "1")

            if last_char != "0":
                generate_strings(current + "0", "0")

        generate_strings("")

        return results


# @leet end
