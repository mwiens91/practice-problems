# @leet start
class Solution:
    def countArrangement(self, n: int) -> int:
        # NOTE: needed ChatGPT to figure out how to do bitmask stuff

        # Recursively count the number of valid arrangements starting
        # from a given state represented by:
        #
        # - a bitmask which indicates which numbers from 1 through n are
        # used so far in the arrangement
        # - a position which indicates which position of the arrangement
        # we are currently filling
        #
        # We memoize on the bitmask and position.
        memo: dict[tuple[int, int], int] = {}

        def count_from_state(mask: int, pos: int) -> int:
            if pos > n:
                # If we've filled the final position, we will
                # recursively call this function and arrive here,
                # returning 1
                return 1

            # Check for cached result
            if (key := (mask, pos)) in memo:
                return memo[key]

            # Count the number of valid arrangements from this state
            count = 0

            # For the bitwise operations used here,
            #
            # - mask & (1 << (num - 1)) checks if a 1 bit is set in the
            # mask for the number we are iterating over
            # - mask | (1 << (num - 1)) sets a bit to 1 for the number
            # we are iterating over
            for num in range(1, n + 1):
                if not (mask & (1 << (num - 1))) and (num % pos == 0 or pos % num == 0):
                    count += count_from_state(mask | (1 << (num - 1)), pos + 1)

            # Cache and return count
            memo[(mask, pos)] = count

            return count

        return count_from_state(0, 1)


# @leet end
