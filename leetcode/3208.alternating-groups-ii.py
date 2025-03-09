# @leet start
class Solution:
    def numberOfAlternatingGroups(self, colors: list[int], k: int) -> int:
        # Create a list with indices corresponding to the colours list
        # where elements are True if they are surrounded by different
        # colours and False otherwise
        n = len(colors)

        is_different: list[bool] = [False] * n

        for i in range(n):
            # Check if the left and right colours are the same and are
            # different from the current colour
            if colors[i - 1] == colors[(i + 1) % n] != colors[i]:
                is_different[i] = True

        # An alternating group exists for every consecutive group of
        # k - 2 elements that have different neighbours. We find the
        # answer by counting how many of these consecutive groups exist.
        # We use a sliding window and count the number of elements with
        # different neighbours. We'll initialize the first window before
        # sliding.
        window_size = k - 2

        num_true_in_window = sum(int(is_different[i]) for i in range(window_size))

        alternating_group_count = int(num_true_in_window == window_size)

        for i in range(1, n):
            # Slide the window
            num_true_in_window -= int(is_different[i - 1])
            num_true_in_window += int(is_different[(i - 1 + window_size) % n])

            # Add to group count
            alternating_group_count += int(num_true_in_window == window_size)

        return alternating_group_count


# @leet end
