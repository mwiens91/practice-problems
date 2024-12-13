# @leet start
class Solution:
    def numSquares(self, n: int) -> int:
        # Generate a set of perfect squares up to n
        perfect_squares = set()

        x = 1

        while (x_sq := x**2) <= n:
            perfect_squares.add(x_sq)
            x += 1

        # Handle edge case where n is a perfect square
        if n in perfect_squares:
            return 1

        # Now to find how many numbers perfect squares are needed,
        # suppose we are testing to see if it's possible to form n with
        # N perfect squares. To accomplish this we iterate through each
        # perfect square x^2 and see if n can be formed using x^2 + y,
        # where y is the sum of any N - 1 perfect squares. We keep track
        # of the sums of N - 1 perfect squares in a cache.
        N = 2

        # This holds the sums of N - 1 perfect squares
        cache = perfect_squares.copy()

        while True:
            # This will be the cache for the next iteration
            next_cache = set()

            # Find the sum of all N perfect squares
            for perfect_square in perfect_squares:
                for prev_sum in cache:
                    new_sum = perfect_square + prev_sum

                    # Get out if we've found n
                    if new_sum == n:
                        return N

                    # Otherwise get out, and add to cache (but only if
                    # the sum is less than n—zero point keeping it
                    # otherwise)
                    if new_sum < n:
                        next_cache.add(new_sum)

            # Set up for next iteration
            cache = next_cache
            N += 1


# @leet end
