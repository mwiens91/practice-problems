# @leet start
import math


class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        # We want to process each contiguous chunk of 0s which are not
        # adjacent to 1s
        new_flowers_possible = 0

        num_flowerbeds = len(flowerbed)
        i = 0

        while i < num_flowerbeds:
            # Skip to the first 0 not adjacent to a 1
            while i < num_flowerbeds and flowerbed[i] == 1:
                # Skip a 1
                i += 1

            if i > 0 and flowerbed[i - 1] == 1:
                # Skip the first 0 after a 1
                i += 1

            # Count the number of zeroes and add to the number of
            # new flowers possible count
            num_contiguous_zeroes = 0

            while (
                i < num_flowerbeds
                and flowerbed[i] == 0
                and (i == num_flowerbeds - 1 or flowerbed[i + 1] == 0)
            ):
                num_contiguous_zeroes += 1
                i += 1

            new_flowers_possible += math.ceil(num_contiguous_zeroes / 2)

            # Set up for next iteration. We're either at the end of
            # the flowerbed array or we're at a 0 that has a 1 as a
            # next element. We need to skip past this 0 in the
            # latter case.
            i += 1

        # Return if n new flowers are possible
        return new_flowers_possible >= n


# @leet end
