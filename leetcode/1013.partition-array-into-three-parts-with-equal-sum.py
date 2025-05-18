# @leet start
class Solution:
    def canThreePartsEqualSum(self, arr: list[int]) -> bool:
        FAILURE = -1

        # Each partition must have 1/3 of the array sum
        array_sum = sum(arr)

        if array_sum % 3 != 0:
            return False

        target_sum = array_sum // 3

        # Define a function to find the index at which target_sum occurs
        # in the partial sums of a suffix of arr starting at a given
        # start index. If no such index exists, return -1.
        n = len(arr)

        def find_partial_sum_idx_of_target_sum(start_idx: int) -> int:
            partial_sum = 0

            i = start_idx

            while i < n:
                partial_sum += arr[i]

                if partial_sum == target_sum:
                    return i

                i += 1

            return FAILURE

        # Return whether there are three partitions which equal target sum
        partition_start_idx = 0

        for _ in range(3):
            partition_end_idx = find_partial_sum_idx_of_target_sum(partition_start_idx)

            if partition_end_idx == FAILURE:
                return False

            partition_start_idx = partition_end_idx + 1

        return True


# @leet end
