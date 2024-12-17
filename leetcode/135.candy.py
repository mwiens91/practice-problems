# @leet start
import math


class Solution:
    def candy(self, ratings: list[int]) -> int:
        # Get number of ratings/children
        n = len(ratings)

        # The solution we'll do is O(1) memory, and it's pretty tricky
        # to explain without drawing out examples; that said, with
        # examples, it's really not too complicated. I'll give a shot at
        # explaining anyway. The general idea is when we have runs of
        # ascending ratings, we increase each subsequent number of
        # candies distributed by one, keeping track of the peak. When
        # we have runs of descending ratings, we start at one and count
        # upwards by one. While in our code we would assign candies 1,
        # 2, ..., m; in the actual solution this corresponds to giving
        # the first child in the run m candies, and decreasing by one as
        # we go along. What's happening in our code is essentially
        # reversed for a descending run, but the total ends up being the
        # same. In the case that m is greater than or equal to our peak,
        # we need to retroactively adjust the previous peak, and add
        # more candies to it to make sure that the peak is always larger
        # than m.

        # Store total number of candies here
        candies = 1

        # Keep track of previous peaks and run lengths
        prev_peak = math.inf
        run_length = 1

        # Keep track of whether we are ascending or descending. We start
        # off assuming we are descending.
        ascending = False
        descending = True

        for i in range(1, n):
            prev_rating = ratings[i - 1]
            this_rating = ratings[i]

            if this_rating > prev_rating:
                # We're ascending. What we do depends on if we've just
                # started ascending or if we're in the midst of
                # ascending.
                if not ascending:
                    # We've just started ascending. First set boolean
                    # vars.
                    ascending = True
                    descending = False

                    # Now set run length
                    run_length = 2
                else:
                    # We've already been ascending. Update run length.
                    run_length += 1

                # Add candies
                candies += run_length
            elif this_rating < prev_rating:
                # We're descending. Like above, what we do depends on
                # whether we've just started descending.
                if not descending:
                    # Set boolean vars
                    ascending = False
                    descending = True

                    # Update peak
                    prev_peak = run_length

                    # Set run length
                    run_length = 1
                else:
                    # Update run length
                    run_length += 1

                # If our current number of candies is equal or
                # greater to the previous peak, add one candy to the
                # total to fixup what the previous peak's number of
                # candies should have been
                if run_length >= prev_peak:
                    candies += 1

                # Add candies
                candies += run_length
            else:
                # this_rating == prev_rating
                # Reset to initial state, and add one candy
                ascending = False
                descending = True

                prev_peak = math.inf
                run_length = 1

                candies += 1

        return candies


# @leet end
