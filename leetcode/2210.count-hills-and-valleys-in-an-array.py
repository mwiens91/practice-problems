# @leet start
class Solution:
    def countHillValley(self, nums: list[int]) -> int:
        n = len(nums)

        # Get i to the first index that has an element different from
        # the first element
        i = 1
        prev = nums[0]

        while i < n - 1 and nums[i] == prev:
            i += 1

        # Count hills and valleys
        count = 0

        while i < n - 1:
            current = nums[i]

            # Move i to the next index that has an element different
            # from the current number
            i += 1

            while i < n - 1 and nums[i] == current:
                i += 1

            next_ = nums[i]

            if prev < current and next_ < current:
                count += 1
            elif prev > current and next_ > current:
                count += 1

            # Set up for next iteration
            prev = current

        return count


# @leet end
