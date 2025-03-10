# @leet start
class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        # Disclaimer: I needed help from ChatGPT for this one because
        # I'm not super familiar with probabilities.

        # Edge case: if k == 0 the probability of obtaining any number
        # of points is 1. Conditional optimization: if n exceeds k by
        # maxPts, the probability of obtaining less than or equal to n
        # points is 1.
        if k == 0 or n >= k + maxPts:
            return 1

        # Assume k > 0. The probability of obtaining n or fewer points
        # is given by the sum
        #
        # P(k) + P(k + 1) + ... + P(n).
        #
        # The probabality of obtaining exactly x points is, for
        # maxPts <= x < k,
        #
        # (P(x - 1) + P(x - 2) + ... + P(x - maxPts)) / maxPts.
        #
        # The sum P(x - 1) + ... + P(x - maxPts) is the sum of
        # probabilities of being in previous states where we can draw a
        # new number and reach x. The last term 1 / maxPts is the
        # probability of drawing a new number between 1 and maxPts.
        #
        # For x < maxPts, the probability is
        #
        # (P(x - 1) + P(x - 2) + ... + P(0)) / maxPts;
        #
        # because we start at 0 points.
        #
        # For k <= x < k + maxPts, since we can't draw after k points,
        # the probability is
        #
        # (P(k - 1) + P(k - 2) + P(x - maxPts)) / maxPts
        #
        # where j = x - k.
        #
        # For x >= k + maxPts the probability is 0.
        #
        # We will find probabilities up to n bottom up, and, as an
        # optimization, keep the sum of probabilities of being in a
        # previous state where we can draw to get to the desired state
        # in a single variable.
        probabilities: list[float] = [0] * (n + 1)
        probabilities[0] = 1

        # We start with 0 points, with probability 1
        previous_state_probability = 1

        for num in range(1, n + 1):
            # Calculate probability to obtain exactly num points
            probabilities[num] = previous_state_probability / maxPts

            # Update the previous state probability for the next
            # iteration. Add this state if num < k.
            if num < k:
                previous_state_probability += probabilities[num]

            # Subtract the num - maxPts state if num >= maxPts
            if num >= maxPts:
                previous_state_probability -= probabilities[num - maxPts]

        # Return the sum of probabilities of obtaining exactly x points,
        # k <= x <= n
        return sum(probabilities[-(n - k + 1) :])


# @leet end
