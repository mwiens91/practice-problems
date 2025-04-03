# @leet start
class Solution:
    def mostPoints(self, questions: list[list[int]]) -> int:
        # Here's the idea: we go through questions in reverse order and
        # for each question try taking the next best available question.
        # We can do this by keeping track of the maximums seen so far.
        # Note that we could do this in O(1) memory by modifying the
        # original input, but it's a lot uglier that way, so I haven't
        # done that.
        n = len(questions)

        max_seen = [questions[-1][0]] * n

        for i in range(n - 2, -1, -1):
            points, brainpower = questions[i]

            try:
                points += max_seen[i + brainpower + 1]
            except IndexError:
                pass

            max_seen[i] = max(points, max_seen[i + 1])

        return max_seen[0]


# @leet end
