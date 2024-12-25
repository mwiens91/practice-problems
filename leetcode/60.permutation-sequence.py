# @leet start
from math import factorial


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # We note that for a given n, the first (n - 1)! permutations
        # have 1 as the first digit, the next (n - 1)! permutations have
        # 2 as the first digit, etc. Generally, for j = 1, ..., n, the
        # permutations (j - 1)(n - 1)! + 1 to j(n - 1)! have j as
        # their first digit.
        #
        # Our strategy here will be to find the first digit using all
        # selecting from numbers 1, 2, ..., n; then once we've chosen a
        # number, say x as the first digit, treat the remainder as a new
        # permutation containing numbers from {1, 2, ..., n} \ {x}. We
        # succesively find the first digits of each new permutation
        # until there are no numbers left.

        # This list will contain what digits we have to choose from.
        # Once we use a digit, we'll mark it with None in the list.
        # We'll also define a helper function to get the jth digit from
        # the available digits.
        available_digits: list[int | None] = list(range(1, n + 1))

        def get_jth_digit(j: int) -> int:
            """Get the jth available digit and mark is as None.

            j is 1-indexed.

            Not going to worry about going out of index here, since j
            will always be <= the number of available digits when we
            call this.
            """
            # i keeps track of the index in available_digits.
            # current_digit_number keeps track what available digit
            # we're looking at (the 1st, 2nd, etc.)
            i = 0
            current_digit_number = 1

            while True:
                # Get the digit under the index
                current_digit = available_digits[i]

                if current_digit is not None:
                    # Digit is valid, if we're looking at the jth digit,
                    # return it; else increment the current digit
                    # counter
                    if current_digit_number == j:
                        # Mark the digit we're going to return as
                        # already used
                        available_digits[i] = None

                        return current_digit

                    current_digit_number += 1

                # Set up for next iteration
                i += 1

        # Now we find the result
        result: list[int] = [0] * n

        for i in range(n):
            # Find the next digit number (i.e., first available, second
            # available, etc.) for the currene permutation. Suppose the
            # current permutation has length m. Then the first digit is
            # given by 1 + (k - 1) // (m - 1)!.
            factorial_result = factorial(n - i - 1)
            next_digit_number = 1 + (k - 1) // factorial_result

            # Put the next digit in the result
            result[i] = get_jth_digit(next_digit_number)

            # Update k for the next permutation: subtract all multiples
            # of (m - 1)!
            k -= (next_digit_number - 1) * factorial_result

        return "".join([str(x) for x in result])


# @leet end
