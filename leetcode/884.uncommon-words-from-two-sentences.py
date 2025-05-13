# @leet start
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:
        seen_once = set()
        seen_multiple = set()

        for s in [s1, s2]:
            for word in s.split():
                if word in seen_once:
                    # Deal with an word seen once already
                    seen_once.remove(word)
                    seen_multiple.add(word)
                elif word not in seen_multiple:
                    # Deal with a word not seen before
                    seen_once.add(word)

        return list(seen_once)


# @leet end
