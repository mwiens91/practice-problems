# @leet start
class Solution:
    def validateStackSequences(self, pushed: list[int], popped: list[int]) -> bool:
        stack: list[int] = []

        n = len(popped)
        popped_idx = 0

        for num in pushed:
            # Push next element onto stack
            stack.append(num)

            # Pop as much as we can
            while stack and popped_idx < n and popped[popped_idx] == stack[-1]:
                stack.pop()
                popped_idx += 1

        return not bool(stack)


# @leet end
