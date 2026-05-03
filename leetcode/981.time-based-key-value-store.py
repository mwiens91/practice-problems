# @leet start
class TimeMap:

    def __init__(self):
        self.map: dict[str, list[tuple[int, str]]] = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = []

        self.map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""

        arr = self.map[key]

        left = 0
        right = len(arr) - 1

        while left <= right:
            mid = (left + right) // 2

            if arr[mid][0] <= timestamp:
                left = mid + 1
            else:
                right = mid - 1

        return arr[right][1] if right != -1 else ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
# @leet end
