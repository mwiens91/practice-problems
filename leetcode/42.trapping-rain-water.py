# @leet start
class Solution:
    def trap(self, height: list[int]) -> int:
        # NOTE: I needed to use NeetCode to get the gist of how to think
        # about solving this problem

        # Use a two-pointer solution. Here's the idea: suppose for a
        # given index with height h we know the maximum height on the
        # left max_left and the maximum height on the right max_right;
        # then the amount of water from that index that will contribute
        # to the total area is given by
        #
        # max(
        #   0,
        #   min(max_left, max_right) - h
        # )
        #
        # We can solve this with O(n) memory by creating two arrays
        # containing max_lefts and max_rights for each element. This can
        # also be done in O(1) memory by using two pointers—one moving
        # forward from the left i and one moving backward from the right
        # j—and keeping track of the max_left and max_right seen so far.
        # We move the pointer corresponding to the min of those maxes.
        # Then, whenever we encounter an element with height h, the
        # formula above still holds, because the minimum of max_left and
        # max_right will be just as it was with the other approach
        # (because we move the pointer with the min of the maxes).
        i = 0
        j = len(height) - 1

        # Set this up so we start moving with the left pointer. We could
        # do this the other way around and set max_right to 0, max_left
        # to height[0] and start with the right pointer. Either works.
        max_left = 0
        max_right = height[j]

        moving_left = True
        area = 0

        # Because of how we're switching our pointers, i == j is okay
        # here: we won't process any index twice
        while i <= j:
            # Grab the height of the current index
            h = 0

            if moving_left:
                h = height[i]
            else:
                h = height[j]

            # Add to the area
            area += max(0, min(max_left, max_right) - h)

            # Update one of the maximums and move the pointer
            if moving_left:
                max_left = max(max_left, h)
                i += 1
            else:
                max_right = max(max_right, h)
                j -= 1

            # Update direction
            moving_left = max_left <= max_right

        return area
# @leet end
