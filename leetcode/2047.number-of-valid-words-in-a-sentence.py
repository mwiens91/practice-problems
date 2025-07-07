# @leet start
class Solution:
    def countValidWords(self, sentence: str) -> int:
        PUNCTUATION = {"!", ".", ","}
        HYPHEN = "-"

        valid_word_count = 0

        for word in sentence.split():
            hyphen_count = 0

            for i, char in enumerate(word):
                if char.isdigit():
                    # Digits not allowed
                    break

                if char in PUNCTUATION and i != len(word) - 1:
                    # Punctuation only allowed at end of word
                    break

                if char == HYPHEN:
                    if (
                        hyphen_count == 1
                        or i in {0, len(word) - 1}
                        or not word[i + 1].isalpha()
                    ):
                        # Hyphers must be surrounded by letters
                        #
                        # NOTE: we didn't need to check the previous letter
                        # because the only invalid character that could have
                        # come before would have been a hypen, but in that
                        # case the above check would have already failed for
                        # that hyphen because the next character would have
                        # been a hyphen.
                        break

                    hyphen_count += 1

            else:
                valid_word_count += 1

        return valid_word_count


# @leet end
