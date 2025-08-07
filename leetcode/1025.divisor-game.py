# @leet start
class Solution:
    def divisorGame(self, n: int) -> bool:
        # Whoever gets to n = 1 loses. Whoever is at an even number can
        # force the opponent to have an odd number on the next turn. In
        # response, the opponent must give back an even number on the
        # next round; this is because an odd number only has odd
        # divisors and the number they return will be the difference of
        # an odd number and another odd number, which is an even
        # number. Thus, if someone arrives at an even number they can
        # force the opponent to eventually have n = 1, and the opponent
        # will lose
        return n % 2 == 0

# @leet end
