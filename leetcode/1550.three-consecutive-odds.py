# @leet start
class Solution:
    def threeConsecutiveOdds(self, arr: list[int]) -> bool:
        consecutive_count = 0

        for num in arr:
            if num % 2 == 1:
                consecutive_count += 1

                if consecutive_count == 3:
                    return True
            else:
                consecutive_count = 0

        return False


# @leet end
