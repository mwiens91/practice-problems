# @leet start
from string import ascii_lowercase


class Solution:
    def calculateScore(self, s: str) -> int:
        # Define a function to find the mirror of a letter
        def get_mirror(char: str) -> str:
            return chr(ord("a") + ord("z") - ord(char))

        # Create a dictionary of stacks for each letter which contain
        # indices which contain that letter
        letter_stacks_dict: dict[str, list[int]] = {
            letter: [] for letter in ascii_lowercase
        }

        # For each letter, get the closest mirrored letter and add the
        # index difference to the score; if there is no closest mirrored
        # letter, keep track of the index of this letter on the stack.
        score = 0

        for idx, letter in enumerate(s):
            if mirror_letter_stack_dict := letter_stacks_dict[get_mirror(letter)]:
                score += idx - mirror_letter_stack_dict.pop()
            else:
                letter_stacks_dict[letter].append(idx)

        return score


# @leet end
