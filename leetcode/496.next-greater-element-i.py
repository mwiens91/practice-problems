# @leet start
class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        # First build a dictionary using nums1 as keys
        next_greater_elements_dict = {x: -1 for x in nums1}

        # Now find each next greater element using a stack
        stack = []

        for num in nums2:
            # Assign this as the next greater element to any numbers at
            # the top of the stack that this number is greater than
            while stack and stack[-1] < num:
                top_of_stack_num = stack.pop()

                next_greater_elements_dict[top_of_stack_num] = num

            # Put the number on the stack if the number is also in nums1
            if num in next_greater_elements_dict:
                stack.append(num)

        # Build up the final result
        nums1_length = len(nums1)

        result = [0] * nums1_length

        for i in range(nums1_length):
            result[i] = next_greater_elements_dict[nums1[i]]

        return result


# @leet end
