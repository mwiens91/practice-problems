# @leet start
import math


class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        # The thing we'll make use of here is the fact that each
        # temperature lies between 30 and 100. This means that if we use
        # an array where each index represents a possible temperature,
        # this array will take O(1) memory and modifying or traversing
        # the array will take O(1) time.
        #
        # The idea for this algorithm is to traverse the temperatures in
        # reverse order. As we move backwards we modify an array
        # next_warmer_temps which has 71 elements, each index i
        # representing the temperature i + 30, containing the nearest
        # element j in the temperatures list that is warmer. Before
        # modifying this array, however, we check the array to see when
        # the next warmer day will be, and append that to our results.

        # Set up next_warmer_temps array
        INDEX_TO_TEMP_OFFSET = 30
        next_warmer_temps = [math.inf] * 71

        # This will hold our results that we collect from backwards
        # iterating. We'll insert our answers from the back to the
        # front.
        n = len(temperatures)
        res = [0] * n

        # Do the procedure described above. We skip the very last
        # element since there will never be a next warmer day for it.
        for i in range(n - 2, -1, -1):
            temp = temperatures[i]

            # Get result. If there is no warmer temperature upcoming
            # just keep the default value of 0.
            if (
                next_warmer_temp := next_warmer_temps[temp - INDEX_TO_TEMP_OFFSET]
            ) != math.inf:
                res[i] = next_warmer_temp - i

            # Modify array
            for j in range(temp - INDEX_TO_TEMP_OFFSET):
                next_warmer_temps[j] = i

        return res


# @leet end
