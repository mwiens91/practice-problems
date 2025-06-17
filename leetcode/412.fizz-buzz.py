# @leet start
class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        # Setup result with the default result
        result = [str(i) for i in range(1, n + 1)]

        # Replace results with specific words where appropriate
        for i in range(1, n + 1):
            words_for_idx: list[str] = []

            if i % 3 == 0:
                words_for_idx.append("Fizz")

            if i % 5 == 0:
                words_for_idx.append("Buzz")

            if words_for_idx:
                result[i - 1] = "".join(words_for_idx)

        return result


# @leet end
