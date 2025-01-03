# @leet start
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        # Results here
        results = []

        # Numbers used in a given iteration here
        nums_used = []

        def get_combination_sums(current_num: int, nums_left: int, target: int) -> None:
            # Get out if the current number is bigger than 9 or the
            # current number is bigger than the target
            if current_num > 9 or current_num > target:
                return

            # If there's one number left, add the result if it's
            # possible and get out
            if nums_left == 1:
                if current_num <= target <= 9:
                    results.append(nums_used + [target])

                return

            # Recurse, either using this number or skipping it
            nums_used.append(current_num)

            get_combination_sums(
                current_num + 1,
                nums_left - 1,
                target - current_num,
            )

            nums_used.pop()

            get_combination_sums(
                current_num + 1,
                nums_left,
                target,
            )

        get_combination_sums(1, k, n)

        return results


# @leet end
