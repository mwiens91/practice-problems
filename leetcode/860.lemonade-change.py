# @leet start
class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        # Simulate the problem
        num_5s = 0
        num_10s = 0

        for bill in bills:
            if bill == 20:
                # If a bill is 20 try giving change with a 10 + 5
                # first; 5 + 5 + 5 if that isn't possible
                if num_10s > 0 and num_5s > 0:
                    num_10s -= 1
                    num_5s -= 1
                elif num_5s >= 3:
                    num_5s -= 3
                else:
                    return False
            elif bill == 10:
                if num_5s > 0:
                    num_10s += 1
                    num_5s -= 1
                else:
                    return False
            else:
                # bill == 5
                num_5s += 1

        return True


# @leet end
