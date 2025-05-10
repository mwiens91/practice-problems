# @leet start
class Solution:
    def capitalizeTitle(self, title: str) -> str:
        title_split = title.split()

        for i, word in enumerate(title_split):
            if len(word) <= 2:
                title_split[i] = title_split[i].lower()
            else:
                title_split[i] = title_split[i].capitalize()

        return " ".join(title_split)


# @leet end
