# @leet start
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        # Get a count of each character in s in the custom ordering and
        # the "remainder": the chars in s, in their respective order,
        # that are not part of the custom ordering
        chars_in_order_counts: dict[str, int] = {char: 0 for char in order}
        remainder: list[str] = []

        for char in s:
            if char in chars_in_order_counts:
                chars_in_order_counts[char] += 1
            else:
                remainder.append(char)

        # Build the resulting string
        result: list[str] = []

        for char in order:
            result.extend([char] * chars_in_order_counts[char])

        result.extend(remainder)

        return "".join(result)


# @leet end
