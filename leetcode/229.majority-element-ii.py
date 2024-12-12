# @leet start
class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        # For this problem there can be at most two elements that occur
        # more than n // 3 times. I needed to use Neetcode to really get
        # how to do this. The solution isn't yet 100% inituitive for me
        # yet, but it seems plausible.

        # This map holds at most 2 key-value pairs. At the end of the
        # following loop, any keys in the dictionary are candidates for
        # being majority elements. Note that the values are not absolute
        # counts.
        count_map = {}

        for num in nums:
            if num in count_map:
                # Increase count if we're already there
                count_map[num] += 1
            else:
                if len(count_map) <= 2:
                    # Add the value
                    count_map[num] = 1
                else:
                    # Decrement all counts in the count map and delete
                    # any entries containing zero
                    keys_to_delete = []

                    for key in count_map:
                        count_map[key] -= 1

                        if not count_map[key]:
                            keys_to_delete.append(key)

                    for key in keys_to_delete:
                        del count_map[key]

        # Now see if any candidates meet threshold
        threshold = len(nums) // 3

        res = []

        for candidate in count_map:
            if nums.count(candidate) > threshold:
                res.append(candidate)

        return res


# @leet end
