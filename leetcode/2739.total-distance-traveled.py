# @leet start
class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        # Either the maximum number of injections is limited by the main
        # tank fuel M or the additional fuel A. If we are limited by A,
        # then t = A. If we are limited by M, then the first injection
        # costs 5 fuel from M and each subsequent injection costs 4:
        #
        # M >= 5 + (t - 1)4
        # => t <= (M - 1) / 4
        # => t = (M - 1) // 4
        return 10 * (mainTank + min((mainTank - 1) // 4, additionalTank))


# @leet end
