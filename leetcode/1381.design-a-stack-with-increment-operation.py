# @leet start
class CustomStack:

    def __init__(self, maxSize: int):
        self.stack: list[int] = []
        self.inc: list[int] = []
        self.max = maxSize

    def push(self, x: int) -> None:
        if len(self.stack) < self.max:
            self.stack.append(x)
            self.inc.append(0)

    def pop(self) -> int:
        if not self.stack:
            return -1

        if len(self.stack) > 1:
            self.inc[-2] += self.inc[-1]

        return self.stack.pop() + self.inc.pop()

    def increment(self, k: int, val: int) -> None:
        if self.stack:
            self.inc[min(k, len(self.stack)) - 1] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
# @leet end
