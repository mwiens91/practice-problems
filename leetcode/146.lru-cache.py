# @leet start
from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity: int):
        # Map stores two_tuples
        self.map: OrderedDict[int, int] = OrderedDict()
        self.capacity: int = capacity

    def get(self, key: int) -> int:
        if key in self.map:
            self.map.move_to_end(key)

            return self.map[key]

        return -1

    def put(self, key: int, value: int) -> None:
        is_update = key in self.map

        if len(self.map) == self.capacity and not is_update:
            self.map.popitem(last=False)

        self.map[key] = value

        if is_update:
            self.map.move_to_end(key)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @leet end
