# @leet start
class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        good_substrings_of_length_three = 0

        for first, second, third in zip(s, s[1:], s[2:]):
            if first != second and second != third and first != third:
                good_substrings_of_length_three += 1

        return good_substrings_of_length_three


# @leet end
