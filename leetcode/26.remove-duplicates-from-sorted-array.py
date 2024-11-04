# @leet start
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        # Keep track of number of unique numbers k and replace any
        # duplicates with subsequent unique numbers using two pointers.
        # First, we'll find the first duplicate index i (if it exists).
        # Second, from i we'll find the next unique index j (if it
        # exists). Third, we'll swap the numbers in i and j, increment
        # i. Then repeat the second and third steps until we're out of
        # bounds.
        k = 1

        n = len(nums)
        last_unique_num = nums[0]

        i = 1
        j = 1

        # Find first duplicate
        while i < n:
            if (num := nums[i]) != last_unique_num:
                i += 1
                k += 1

                last_unique_num = num
            else:
                break

        # Find next unique number
        j = i + 1

        while j < n:
            if (num := nums[j]) > last_unique_num:
                # Found unique num: swap
                nums[i], nums[j] = nums[j], nums[i]

                # Continue finding next unique number, incrementing i
                i += 1
                j = i + 1

                last_unique_num = num
                k += 1
            else:
                # Still duplicate
                j += 1

        return k
# @leet end
