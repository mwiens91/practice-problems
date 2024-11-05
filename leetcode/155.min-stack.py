# @leet start
class MinStack:

    def __init__(self):
        # Vals will hold the values. For a value in vals, the
        # corresponding index in min_vals will contain the minimum value
        # seen in the stack at the time of the value's insertion.
        self.vals = []
        self.min_vals = []

    def push(self, val: int) -> None:
        self.vals.append(val)

        if self.min_vals:
            self.min_vals.append(min(val, self.min_vals[-1]))
        else:
            self.min_vals.append(val)

    def pop(self) -> None:
        self.vals.pop()
        self.min_vals.pop()

    def top(self) -> int:
        return self.vals[-1]

    def getMin(self) -> int:
        return self.min_vals[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @leet end

