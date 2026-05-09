# @leet start
class Solution:
    def scoreValidator(self, events: list[str]) -> list[int]:
        MAX_COUNT = 10
        score = 0
        count = 0

        i = 0

        while i < len(events) and count < MAX_COUNT:
            if events[i] == "W":
                count += 1
            elif events[i] in ("WD", "NB"):
                score += 1
            else:
                score += int(events[i])

            i += 1

        return [score, count]


# @leet end
