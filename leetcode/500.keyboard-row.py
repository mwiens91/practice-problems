# @leet start
class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        row_sets = (
            set("qwertyuiop"),
            set("asdfghjkl"),
            set("zxcvbnm"),
        )

        def contained_in_row(word: str) -> bool:
            for row_set in row_sets:
                if set(word.lower()).issubset(row_set):
                    return True

            return False

        return [word for word in words if contained_in_row(word)]


# @leet end
