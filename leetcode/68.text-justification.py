# @leet start
class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        result: list[str] = []

        i = 0
        num_words = len(words)

        while i < num_words:
            # Get the words in this line
            line_words = [words[i]]
            remaining_width = maxWidth - len(words[i])
            i += 1

            while i < num_words and len(words[i]) + 1 <= remaining_width:
                line_words.append(words[i])
                remaining_width -= len(words[i]) + 1
                i += 1

            # Add in the spacing—how we do this depends on whether we're
            # at the last line
            num_line_words = len(line_words)

            if i < num_words:
                # Not last line
                if num_line_words == 1:
                    gap_width = 0
                    extra = 0
                    suffix = remaining_width
                else:
                    spaces = maxWidth - sum(len(word) for word in line_words)

                    gap_width = spaces // (num_line_words - 1)
                    extra = spaces % (num_line_words - 1)
                    suffix = 0
            else:
                # Last line
                gap_width = 1
                extra = 0
                suffix = remaining_width

            line_result: list[str] = []

            for j, word in enumerate(line_words):
                num_spaces = gap_width if j < num_line_words - 1 else 0

                if extra:
                    num_spaces += 1
                    extra -= 1

                line_result.extend([word, " " * num_spaces])

            line_result.append(" " * suffix)

            result.append("".join(line_result))

        return result


# @leet end
