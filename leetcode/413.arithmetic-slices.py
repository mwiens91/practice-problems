# @leet start
class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        n = len(nums)

        # We'll go through arithmetic sequences starting at a given
        # index and get as many subarrays as possible from each
        # sequence
        num_arithmetic_subarrays = 0

        start_idx = 0

        while start_idx <= n - 3:
            # For each arithmetic sequence, starting from index i and
            # ending at index j (inclusive) with j - i >= 2 (there are
            # at least 3 elements in the sequence), there are j - i - 1
            # arithmetic subarrays containing the jth element
            # contributed by this sequence. For example, consider the
            # sequence 0, 1, 2, 3. Here j - i = 3. There are
            # j - i - 1 = 2 arithmetic subarrays contributed from this
            # sequence which include the jth element 3: 0, 1, 2 and
            # 0, 1, 2, 3.
            first_difference = nums[start_idx + 1] - nums[start_idx]

            # Extend this sequence as far as possible
            candidate_end_idx = start_idx + 2

            while candidate_end_idx < n:
                if (
                    nums[candidate_end_idx] - nums[candidate_end_idx - 1]
                    != first_difference
                ):
                    # Candidate end index is *not* part of the sequence
                    break

                # Add subarrays contributed by adding the element end
                # index points to
                num_arithmetic_subarrays += candidate_end_idx - start_idx - 1

                candidate_end_idx += 1

            # Reset the start index to point to the end index of the
            # subsequence
            start_idx = candidate_end_idx - 1

        return num_arithmetic_subarrays


# @leet end
