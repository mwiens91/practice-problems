# @leet start
class Solution:
    def replaceWords(self, dictionary: list[str], sentence: str) -> str:
        # For each word in sentence, replace it with the shortest root
        roots_set = set(dictionary)

        words = sentence.split()

        for i, word in enumerate(words):
            # Try matching word with a root
            for substr_end_idx in range(1, len(word)):
                if (substr := word[:substr_end_idx]) in roots_set:
                    # Success! Replace the word and move to next word.
                    words[i] = substr

                    break

        return " ".join(words)


# @leet end
