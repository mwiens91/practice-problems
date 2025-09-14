# @leet start
class Solution:
    def spellchecker(self, wordlist: list[str], queries: list[str]) -> list[str]:
        VOWELS = {"a", "e", "i", "o", "u"}
        VOWEL_MARKER = "0"

        def make_vowels_same(lower_word: str) -> str:
            return "".join(VOWEL_MARKER if ch in VOWELS else ch for ch in lower_word)

        # Lowercase word -> first word match
        lower_dict: dict[str, str] = {}

        # Lower and vowels set to same constant -> first word match
        same_vowel_dict: dict[str, str] = {}

        # Build the dicts
        for word in wordlist:
            lower_word = word.lower()

            if lower_word not in lower_dict:
                lower_dict[lower_word] = word

            same_vowel_word = make_vowels_same(lower_word)

            if same_vowel_word not in same_vowel_dict:
                same_vowel_dict[same_vowel_word] = word

        # Solve the queries
        words = set(wordlist)
        result: list[str] = []

        for word in queries:
            if word in words:
                result.append(word)
            elif (lower_word := word.lower()) in lower_dict:
                result.append(lower_dict[lower_word])
            elif (same_vowel_word := make_vowels_same(lower_word)) in same_vowel_dict:
                result.append(same_vowel_dict[same_vowel_word])
            else:
                result.append("")

        return result


# @leet end
