# @leet start
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # Split the string s
        s_split = s.split()

        # Return False if there's a length mismatch between the number
        # of codes in the pattern and the number of words
        if len(pattern) != len(s_split):
            return False

        # We'll have a bijection between each character (code) in
        # pattern and a word. If everything is consistent we return
        # True; else we return False when we reach an inconsistency.
        code_to_word_dict = {}
        words_seen = set()

        for code, word in zip(pattern, s_split):
            try:
                assert code_to_word_dict[code] == word
            except AssertionError:
                return False
            except KeyError:
                # We haven't encountered this code before. Make sure we
                # haven't given this word a different code.
                if word in words_seen:
                    return False

                # Biject
                code_to_word_dict[code] = word
                words_seen.add(word)

        return True


# @leet end
