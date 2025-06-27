# @leet start
class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        def get_minutes(time: str) -> int:
            return sum(int(comp) * mult for comp, mult in zip(time.split(":"), [60, 1]))

        current_minutes = get_minutes(current)
        correct_minutes = get_minutes(correct)

        ops = 0

        for increment in [60, 15, 5, 1]:
            this_num_ops = (correct_minutes - current_minutes) // increment

            current_minutes += this_num_ops * increment
            ops += this_num_ops

            if current_minutes == correct_minutes:
                break

        return ops


# @leet end
