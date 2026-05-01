# @leet start
class MyQueue:

    def __init__(self):
        self.pushed_raw: list[int] = []
        self.ready: list[int] = []

    def _cycle(self):
        if self.ready:
            return

        while self.pushed_raw:
            self.ready.append(self.pushed_raw.pop())

    def push(self, x: int) -> None:
        self.pushed_raw.append(x)

    def pop(self) -> int:
        self._cycle()

        return self.ready.pop()

    def peek(self) -> int:
        self._cycle()

        return self.ready[-1]

    def empty(self) -> bool:
        self._cycle()

        return not self.ready


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @leet end
