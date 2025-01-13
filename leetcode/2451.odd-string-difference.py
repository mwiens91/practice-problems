# @leet start
class Solution:
    def oddString(self, words: list[str]) -> str:
        # Get the first two difference arrays, convert them to tuples
        word_length = len(words[0])

        def get_difference_tuple(word: str) -> tuple:
            return tuple(
                ord(word[j + 1]) - ord(word[j]) for j in range(word_length - 1)
            )

        difference_tuple_0 = get_difference_tuple(words[0])
        difference_tuple_1 = get_difference_tuple(words[1])

        # If these tuples are different, then one of the first two words
        # has a different difference tuple. Determine which of these
        # words it is by looking at the third difference tuple.
        if difference_tuple_0 != difference_tuple_1:
            difference_tuple_2 = get_difference_tuple(words[2])

            if difference_tuple_0 == difference_tuple_2:
                # Second word has different difference tuple
                return words[1]

            # First word has different difference tuple
            return words[0]

        # Tuples are the same. Iterate through the rest of the words and
        # return the word which has a different difference tuple
        for word in words[2:]:
            if get_difference_tuple(word) != difference_tuple_0:
                return word


# @leet end
