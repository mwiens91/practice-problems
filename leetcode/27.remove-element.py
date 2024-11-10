# @leet start
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        # Idea: use two pointers, one going forwards from the front i;
        # one going backwards from the back j. We start by (1) moving j
        # such that it points to the last non-val integer in nums. Then
        # (2) we move i forward until we encouter val; once we encounter
        # val we swap the values under j and i, and repeat steps (1) and
        # (2) until i == j.
        n = len(nums)

        i = 0
        j = n - 1

        while i < j:
            # Move j backwards until it points to a non-val integer
            while i < j:
                if nums[j] != val:
                    break

                j -= 1

            # Move i forwards until it points to a val integer
            while i < j:
                if nums[i] == val:
                    break

                i += 1

            # Swap and set up for next iteration
            nums[i], nums[j] = nums[j], nums[i]

            i += 1
            j -= 1

        # Return the number of elements not equal to val. When the
        # above loop terminates, the first ith characters have non-val
        # values. We need to check the ith element though, it may or may
        # not be val.
        if not nums or nums[i] == val:
            return i

        return i + 1


# @leet end
