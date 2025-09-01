# @leet start
class Solution:
    def findSubsequences(self, nums: list[int]) -> list[list[int]]:
        # NOTE: used ChatGPT to learn how to do this more elegantly than
        # I otherwise would have
        n = len(nums)
        result: list[list[int]] = []

        def generate_subseqs(start_idx: int, seq: list[int]) -> None:
            if len(seq) >= 2:
                result.append(seq)

            used: set[int] = set()

            for i in range(start_idx, n):
                if nums[i] in used:
                    continue

                if not seq or seq[-1] <= nums[i]:
                    generate_subseqs(i + 1, seq + [nums[i]])
                    used.add(nums[i])

        generate_subseqs(0, [])

        return result


# @leet end
