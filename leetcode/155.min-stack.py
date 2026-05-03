# @leet start
class MinStack:

    def __init__(self):
        self.dec_stack: list[int] = []
        self.stack: list[int] = []

    def push(self, val: int) -> None:
        if not self.dec_stack or val <= self.dec_stack[-1]:
            self.dec_stack.append(val)

        self.stack.append(val)

    def pop(self) -> None:
        res = self.stack.pop()

        if res == self.dec_stack[-1]:
            self.dec_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.dec_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @leet end
