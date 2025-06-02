# @leet start
import re


class Solution:
    def reformatNumber(self, number: str) -> str:
        # NOTE: in retrospect a simpler and faster solution would be to
        # go through number character by character, keeping track of the
        # current group count and inserting dashes when needed
        all_number_chars = re.findall(r"\d", number)

        # Insert all groups of 3 numbers, leaving 0, 2, or 4 digits
        # behind
        result: list[str] = []

        n = len(all_number_chars)

        if n % 3 == 1:
            groups_of_three = n // 3 - 1
        else:
            groups_of_three = n // 3

        for i in range(groups_of_three):
            result.extend(all_number_chars[i * 3 : (i + 1) * 3])
            result.append("-")

        # Insert remaining groups of 2
        num_used_digits = 3 * groups_of_three
        groups_of_two = (n - num_used_digits) // 2

        for i in range(groups_of_two):
            result.extend(
                all_number_chars[
                    num_used_digits + i * 2 : num_used_digits + (i + 1) * 2
                ]
            )
            result.append("-")

        # Pop the trailing "-" that is guaranteed to be in results
        result.pop()

        return "".join(result)


# @leet end
