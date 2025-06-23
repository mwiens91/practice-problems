# @leet start
class Solution:
    def arithmeticTriplets(self, nums: list[int], diff: int) -> int:
        # For each number, count the longest run length of num + diff *
        # diff_mult, processing each number at most once. Use the run
        # length to find the count of arithmetic triplets.
        nums_set = set(nums)
        processed_nums_set: set[int] = set()

        count = 0

        for num in nums:
            if num in processed_nums_set:
                continue

            # Get the maximum run length for this number. No need to add
            # the number to the processed numbers set since we'll never
            # visit it in the loop again anyway.
            run_length = 1
            diff_mult = 1

            while (run_num := num + diff * diff_mult) in nums_set:
                run_length += 1
                diff_mult += 1

                processed_nums_set.add(run_num)

            count += max(0, run_length - 2)

        return count


# @leet end
