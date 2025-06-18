# @leet start
class Solution:
    def findAndReplacePattern(self, words: list[str], pattern: str) -> list[str]:
        def is_word_valid(word: str) -> bool:
            pattern_letter_bijection: dict[str, str] = {}
            used_letters: set[str] = set()

            for letter, pattern_char in zip(word, pattern):
                if pattern_char in pattern_letter_bijection:
                    if pattern_letter_bijection[pattern_char] != letter:
                        # We've already used this pattern character for
                        # a different letter
                        return False
                elif letter in used_letters:
                    # We haven't used this pattern character before but
                    # we have used the letter for a different pattern
                    # character
                    return False
                else:
                    # Add the pattern mapping
                    pattern_letter_bijection[pattern_char] = letter
                    used_letters.add(letter)

            return True

        return list(filter(is_word_valid, words))


# @leet end
