# @leet start
from collections import Counter


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        # Get a counter for digits in the correct place
        digit_chars = [str(x) for x in range(10)]

        digits_in_correct_place_counts = {x: 0 for x in digits}

        for char1, char2 in zip(secret, guess):
            if char1 == char2:
                digits_in_correct_place_counts[char1] += 1

        # Get general counts for both secret and guess
        secret_counts = Counter(secret)
        guess_counts = Counter(guess)

        # Get total number of shared digits
        total_num_shared_digits = 0

        for digit_char in digit_chars:
            total_num_shared_digits += min(
                secret_counts[digit_char], guess_counts[digit_char]
            )

        # Get total number in correct place and total number in
        # incorrect place
        total_in_correct_place = sum(digits_in_correct_place_counts.values())
        total_in_wrong_place = total_num_shared_digits - total_in_correct_place

        return f"{total_in_correct_place}A{total_in_wrong_place}B"


# @leet end
