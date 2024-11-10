# @leet start
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        # Set up an set containing elements in nums
        seen_set = set(nums)

        # Now find longest consecutive sequence. We need to keep track
        # of elements in the seen_set we've already processed.
        best_count = 0
        processed_set = set()

        for num in seen_set:
            if num in processed_set:
                continue

            count = 1

            # See how many consecutive ancestors exist
            temp_num = num

            while temp_num - 1 in seen_set:
                temp_num -= 1
                count += 1

                processed_set.add(temp_num)

            # See how many consecutive children exist
            temp_num = num

            while temp_num + 1 in seen_set:
                temp_num += 1
                count += 1

                processed_set.add(temp_num)

            # Update best count
            best_count = max(best_count, count)

        return best_count


# @leet end
