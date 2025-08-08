# @leet start
class Solution:
    def reorderSpaces(self, text: str) -> str:
        words = text.split()
        num_spaces = text.count(" ")

        num_gaps = len(words) - 1
        num_spaces_between = num_spaces // num_gaps if num_gaps > 0 else 0
        num_spaces_after = num_spaces % num_gaps if num_gaps > 0 else num_spaces

        return (" " * num_spaces_between).join(words) + " " * num_spaces_after


# @leet end
