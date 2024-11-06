# @leet start
class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        # NOTE: Needed NeetCode to understand how to use stack for this.

        # Get length of heights
        n = len(heights)

        # We'll use a stack to keep track of the starting bar of
        # rectangles, and we'll pop from the stack when we cannot
        # continue to extend a rectangle because we've encountered a
        # lower height.
        stack = []
        HEIGHT_IDX = 1

        best_area = 0

        for i, h in enumerate(heights):
            # This is the effective index at which the current h will
            # start. This is so contiguous previous heights that are
            # higher will be used in the area calculation for the lower
            # height.
            start_idx = i

            while stack and h < stack[-1][HEIGHT_IDX]:
                # Cannot extend. Compute area and extend start_idx to
                # left.
                popped_idx, popped_height = stack.pop()

                best_area = max(best_area, (i - popped_idx) * popped_height)
                start_idx = popped_idx

            # Push height onto stack
            stack.append((start_idx, h))

        # Finish consuming stack
        while stack:
            popped_idx, popped_height = stack.pop()
            best_area = max(best_area, (n - popped_idx) * popped_height)

        # Return result
        return best_area
# @leet end

