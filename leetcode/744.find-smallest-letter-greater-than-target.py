# @leet start
class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        # Do a binary search
        n = len(letters)

        left = 0
        right = n - 1

        while left <= right:
            mid = (left + right) // 2

            if letters[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1

        # NOTE: if the target is greater than all letters, then
        # left == n so we return the first letter
        return letters[left % n]


# @leet end
