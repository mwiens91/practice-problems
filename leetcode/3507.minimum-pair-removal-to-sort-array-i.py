# @leet start
class Solution:
    def minimumPairRemoval(self, nums: list[int]) -> int:
        def is_non_decreasing() -> bool:
            for i in range(len(nums) - 1):
                if nums[i + 1] < nums[i]:
                    return False

            return True

        def perform_operation():
            nonlocal nums

            # Find the minimum pair sum and the leftmost left index of
            # the pair that achieves this sum
            minimum_pair_sum = nums[0] + nums[1]
            minimum_pair_sum_left_idx = 0

            for i in range(1, len(nums) - 1):
                if (pair_sum := nums[i] + nums[i + 1]) < minimum_pair_sum:
                    minimum_pair_sum = pair_sum
                    minimum_pair_sum_left_idx = i

            # Replace the leftmost pair achieving the minimum sum with
            # the minimum sum
            nums = (
                nums[:minimum_pair_sum_left_idx]
                + [minimum_pair_sum]
                + nums[minimum_pair_sum_left_idx + 2 :]
            )

        num_operations_required = 0

        # Both checking if the list is non-decreasing and performing the
        # operation are O(n) time per iteration. Theoretically we may be
        # able to perform the operation in O(log(n)) time by using a
        # heap to track all minimum pairs. However, doing this is
        # non-trivial since we need to
        #
        # - remove old pairs that no longer exist
        # - keep track of how indices change when removing elements
        #
        # That said, if we were able to do this, we could bring the
        # total iteration time down to O(log(n) by checking if the list
        # is non-decreasing in O(1) time by keeping track of the total
        # number of inversions and calculating the change in this number
        # when reducing a pair into a single element.
        while True:
            if is_non_decreasing():
                return num_operations_required

            perform_operation()

            num_operations_required += 1


# @leet end
