# @leet start
class Solution:
    def deleteAndEarn(self, nums: list[int]) -> int:
        # Make a dictionary which has nums as keys and count(num) * num
        # as values
        num_sums_dict: dict[int, int] = {}

        for num in nums:
            num_sums_dict[num] = num_sums_dict.get(num, 0) + num

        # Find unique numbers, sort them, and solve this with a memoized
        # recursive function
        unique_nums = sorted(set(nums))
        num_unique_nums = len(unique_nums)

        memo: dict[int, int] = {}

        def get_max_points(idx: int) -> int:
            # Base cases:
            # - if we are at the last unique number, return the sum for
            #   that number
            # - if we are out of bounds, return 0
            if idx >= num_unique_nums - 1:
                try:
                    return num_sums_dict[unique_nums[idx]]
                except IndexError:
                    return 0

            # Try getting a cached result
            if idx in memo:
                return memo[idx]

            # If taking this element prevents us from taking the next element,
            # use the maximum points we get from either
            #
            # - taking this element and skipping the next element
            # - skipping this element
            #
            # Otherwise, take this element.
            if unique_nums[idx + 1] == unique_nums[idx] + 1:
                max_points = max(
                    num_sums_dict[unique_nums[idx]] + get_max_points(idx + 2),
                    get_max_points(idx + 1),
                )
            else:
                max_points = num_sums_dict[unique_nums[idx]] + get_max_points(idx + 1)

            # Memoize and return the result
            memo[idx] = max_points

            return max_points

        return get_max_points(0)


# @leet end
