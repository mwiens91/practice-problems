# @leet start
class Solution:
    def slowestKey(self, releaseTimes: list[int], keysPressed: str) -> str:
        # Iterate through release times and find the key with the
        # longest key press, with the lexicographically highest key
        # being chosen for tie-breaks
        n = len(releaseTimes)

        max_duration = releaseTimes[0]
        max_duration_key = keysPressed[0]

        for i in range(1, n):
            duration = releaseTimes[i] - releaseTimes[i - 1]
            key = keysPressed[i]

            if duration > max_duration or (
                duration == max_duration and key > max_duration_key
            ):
                max_duration = duration
                max_duration_key = key

        return max_duration_key


# @leet end
