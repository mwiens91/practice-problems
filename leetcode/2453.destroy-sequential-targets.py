# @leet start
class Solution:
    def destroyTargets(self, nums: list[int], space: int) -> int:
        # Keep track of the count of integers there are modulo space.
        # Also keep track, for each k, the smallest integer x we've seen
        # such that x % space = k.
        counts_mod_space = {}
        smallest_integer_for_mod_space_value = {}

        for num in nums:
            mod_space_value = num % space

            try:
                counts_mod_space[mod_space_value] += 1
                smallest_integer_for_mod_space_value[mod_space_value] = min(
                    smallest_integer_for_mod_space_value[mod_space_value], num
                )
            except KeyError:
                counts_mod_space[mod_space_value] = 1
                smallest_integer_for_mod_space_value[mod_space_value] = num

        # Find the smallest integer x such that k = x % space has the
        # maximum count in the counts dictionary. First get the maximum
        # count, then find candidate values k = x % space that lead to
        # the highest count. Then, get the minimum x for all k values
        # found above such that k = x % space.
        max_count = max(counts_mod_space.values())
        candidate_mod_space_values = [
            mod_space_value
            for mod_space_value, count in counts_mod_space.items()
            if count == max_count
        ]

        return min(
            smallest_integer_for_mod_space_value[mod_space_value]
            for mod_space_value in candidate_mod_space_values
        )


# @leet end
