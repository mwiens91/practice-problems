# @leet start
class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        # We'll solve this similar to next greater elements I with a
        # stack. We'll put stuff on the stack so long as i < n, but
        # we'll iterate over all but the last element a second time, to
        # deal with the circularity condition.
        n = len(nums)

        # The stack holds two-tuples (num, idx) this time
        NUM_IDX = 0
        # IDX_IDX = 1
        stack: list[tuple[int, int]] = []

        result = [-1] * n

        for i in range(2 * n - 1):
            # Get the number
            num = nums[i % n]

            # Assign result to any elements on the stack that are less
            # than the current number
            while stack and stack[-1][NUM_IDX] < num:
                _, top_of_stack_nums_idx = stack.pop()

                result[top_of_stack_nums_idx] = num

            # Add number to the stack if this is our first iteration of
            # the array
            if i < n:
                stack.append((num, i))

        return result


# @leet end
