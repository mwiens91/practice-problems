# @leet start
class Solution:
    def numTeams(self, rating: list[int]) -> int:
        n = len(rating)
        count = 0

        for i in range(1, n - 1):
            left_smaller = 0
            left_larger = 0

            for j in range(i):
                if rating[j] < rating[i]:
                    left_smaller += 1
                elif rating[j] > rating[i]:
                    left_larger += 1

            right_smaller = 0
            right_larger = 0

            for j in range(i + 1, n):
                if rating[j] < rating[i]:
                    right_smaller += 1
                elif rating[j] > rating[i]:
                    right_larger += 1

            count += left_smaller * right_larger + left_larger * right_smaller

        return count


# @leet end
