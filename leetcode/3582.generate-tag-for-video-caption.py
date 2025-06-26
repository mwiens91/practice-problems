# @leet start
class Solution:
    def generateTag(self, caption: str) -> str:
        words = caption.split()
        first_word = words[0].lower() if words else ""
        remaining_words = "".join(word.title() for word in words[1:])

        return ("#" + first_word + remaining_words)[:100]


# @leet end
