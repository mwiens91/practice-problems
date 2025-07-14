# @leet start
class Solution:
    def uniqueMorseRepresentations(self, words: list[str]) -> int:
        CODE_POINT_LOWER_A = ord("a")
        MORSE_CODE_ALPHABET = [
            ".-",
            "-...",
            "-.-.",
            "-..",
            ".",
            "..-.",
            "--.",
            "....",
            "..",
            ".---",
            "-.-",
            ".-..",
            "--",
            "-.",
            "---",
            ".--.",
            "--.-",
            ".-.",
            "...",
            "-",
            "..-",
            "...-",
            ".--",
            "-..-",
            "-.--",
            "--..",
        ]

        seen_transformations: set[str] = set()

        for word in words:
            seen_transformations.add(
                "".join(
                    [
                        MORSE_CODE_ALPHABET[ord(char) - CODE_POINT_LOWER_A]
                        for char in word
                    ]
                )
            )

        return len(seen_transformations)


# @leet end
