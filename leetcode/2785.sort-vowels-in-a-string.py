# @leet start
class Solution:
    def sortVowels(self, s: str) -> str:
        LOWER_VOWELS = {"a", "e", "i", "o", "u"}

        s_list = list(s)

        vowel_idxs: list[int] = []
        vowels: list[str] = []

        for i, char in enumerate(s_list):
            if char.lower() in LOWER_VOWELS:
                vowel_idxs.append(i)
                vowels.append(char)

        # Re-insert vowels in sorted order
        for i, char in enumerate(sorted(vowels)):
            s_list[vowel_idxs[i]] = char

        return "".join(s_list)


# @leet end
