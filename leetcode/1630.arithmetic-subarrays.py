# @leet start
class Solution:
    def checkArithmeticSubarrays(
        self, nums: list[int], l: list[int], r: list[int]
    ) -> list[bool]:
        # There aren't really any optimizations here, so just directly
        # solve the problem by considering each pair l[i], r[i]
        # independently
        answers: list[bool] = []

        for left_idx, right_idx in zip(l, r):
            # Make sure the difference between successive elements in
            # the sorted subarray are the same
            sorted_subarray = sorted(nums[left_idx : right_idx + 1])

            first_difference = sorted_subarray[1] - sorted_subarray[0]

            for i in range(2, right_idx - left_idx + 1):
                if sorted_subarray[i] - sorted_subarray[i - 1] != first_difference:
                    answers.append(False)

                    break
            else:
                # All differences the same
                answers.append(True)

        return answers


# @leet end
