# @leet start
import math


class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> list[int]:
        # Get the maximum number of normal turns, i.e, turns where we
        # can distribute candies such that on the ith turn we give out i
        # candies. This is the largest integer k such that
        #
        # 1 + 2 + ... + k <= candies
        #
        # and is given by
        #
        # ⌊(sqrt(8*candies + 1) - 1) / 2⌋
        num_normal_turns = int((math.sqrt(8 * candies) - 1) // 2)

        # Get the number of full rounds and the number of remaining
        # normal turns on the last partial round (this is possibly 0)
        num_full_rounds = num_normal_turns // num_people
        num_remainder_normal_turns = num_normal_turns % num_people

        # Distribute candies given out on normal turns. If there are N
        # full rounds and n people, the ith person gets
        #
        # (i + 1) + (i + 1 + n) + ... + (i + 1 + n (N - 1)) candies which
        #
        # simplifies to
        #
        # N (i + 1) + n N (N - 1) / 2
        result = [0] * num_people

        for i in range(num_people):
            result[i] = (
                num_full_rounds * (i + 1)
                + num_people * num_full_rounds * (num_full_rounds - 1) // 2
            )

            # Give last partial round candy
            if i < num_remainder_normal_turns:
                result[i] += i + 1 + num_people * num_full_rounds

        # Give the leftover candy. Recall that the number of normal
        # turns is the largest integer k such that
        #
        # 1 + 2 + ... + k <= candies,
        #
        # where 1 + 2 + ... + k is the number of candy we give out on a
        # normal turn. This can be simplified to
        #
        # k (k + 1) / 2.
        #
        # The number of leftover candies is thus given by
        #
        # candies - k (k + 1) / 2
        result[num_remainder_normal_turns] += (
            candies - num_normal_turns * (num_normal_turns + 1) // 2
        )

        return result


# @leet end
