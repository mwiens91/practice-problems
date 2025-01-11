# @leet start
# NOTE: this solution is not efficient enough. You cannot directly
# simulate this problem, you need to use some kind of trickery.


class Solution:
    def lastRemaining(self, n: int) -> int:
        # Instantiate the array. When we shrink the array, we'll
        # actually just move the stuff we want to keep into the front
        # portion of it; this portion's length will be given by
        # effective_array_length.
        array = list(range(1, n + 1))
        effective_array_length = n

        # Shrink array by removing either even or odd indices
        def shrink_array(remove_even: bool) -> None:
            nonlocal effective_array_length

            # Move the numbers we want to keep to the beginning
            first_empty_idx = int(not remove_even)
            current_idx = first_empty_idx + 1

            while current_idx < effective_array_length:
                # Move number
                array[first_empty_idx] = array[current_idx]

                # Set up for next number to move
                current_idx += 2
                first_empty_idx += 1

            # Update effective array length
            effective_array_length = first_empty_idx

        # To follow the algorithm we repeat the following steps (1)
        # remove all even elements; (2) remove all even elements if the
        # effective length of the array is odd; else remove all odd
        # elements. Before (1) and (2) we check the effective length of
        # the array, returning the only remaining number when the
        # effective length is 1.
        while True:
            if effective_array_length == 1:
                return array[0]

            # Step (1)
            shrink_array(remove_even=True)

            if effective_array_length == 1:
                return array[0]

            # Step (2)
            shrink_array(remove_even=effective_array_length % 2 == 1)


# @leet end
