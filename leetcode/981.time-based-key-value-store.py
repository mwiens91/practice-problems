# @leet start
class TimeMap:

    def __init__(self):
        self.map: dict[str, list[tuple[int, str]]] = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        try:
            self.map[key].append((timestamp, value))
        except KeyError:
            self.map[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        # Return empty string if no values with key or timestamp is less
        # than all keys
        try:
            value_tuples: list[tuple[int, str]] = self.map[key]

            smallest_timestamp = value_tuples[0][0]

            assert smallest_timestamp <= timestamp
        except (KeyError, AssertionError):
            return ""

        # Do a binary search to find the largest timestamp_prev to
        # return the value of such that timestamp_prev <= timestamp
        left = 0
        right = len(value_tuples) - 1

        timestamp_prev_diff = abs(smallest_timestamp - timestamp)
        timestamp_prev_idx = 0

        while left <= right:
            mid = (left + right) // 2
            mid_timestamp = value_tuples[mid][0]

            if mid_timestamp == timestamp:
                timestamp_prev_idx = mid

                break

            if mid_timestamp < timestamp:
                # Update best timestamp_prev candidate
                if (diff := abs(mid_timestamp - timestamp)) < timestamp_prev_diff:
                    timestamp_prev_idx = mid
                    timestamp_prev_diff = diff

                left = mid + 1
            else:
                # mid_timestamp > timestamp
                right = mid - 1

        return value_tuples[timestamp_prev_idx][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
# @leet end
