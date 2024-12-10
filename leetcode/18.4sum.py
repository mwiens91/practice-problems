# @leet start
class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        # Do this in O(n^3) time complexity. There's also a O(n^2)
        # solution, but it's a lot more involved

        # First, sort the input
        nums.sort()

        # Store the answers as tuples in a set
        answers_set: set[tuple[int, int, int, int]] = set()

        # We're going to fix two numbers at a time, then do a 2 pointer
        # solution to find any other two numbers
        n = len(nums)

        for i in range(n):
            first_num = nums[i]

            for j in range(i + 1, n):
                second_num = nums[j]

                effective_target = target - first_num - second_num

                # These two pointers all pairs of numbers with indices
                # > j that sum to the effective target
                k = j + 1
                l = n - 1

                while k < l:
                    third_num = nums[k]
                    fourth_num = nums[l]

                    two_sum = third_num + fourth_num

                    if two_sum < effective_target:
                        k += 1
                    elif two_sum > effective_target:
                        l -= 1
                    else:
                        # two-sum matches effective target. To make sure
                        # all tuples are unique, add them in sorted
                        # order.
                        answers_set.add(
                            tuple(
                                sorted((first_num, second_num, third_num, fourth_num))
                            )
                        )

                        k += 1
                        l -= 1

        return list(answers_set)


# @leet end
