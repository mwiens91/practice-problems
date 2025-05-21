# @leet start
from operator import itemgetter


class Solution:
    def maximumUnits(self, boxTypes: list[list[int]], truckSize: int) -> int:
        # Sort boxes by the number of units in each box in descending
        # order, and consume from the highest unit-yielding boxes
        boxTypes.sort(key=itemgetter(1), reverse=True)

        num_units_on_truck = 0

        box_types_idx = 0
        max_box_types_idx = len(boxTypes) - 1

        while truckSize and box_types_idx <= max_box_types_idx:
            num_boxes_of_type, num_units_per_box = boxTypes[box_types_idx]

            num_boxes_to_consume = min(num_boxes_of_type, truckSize)
            truckSize -= num_boxes_to_consume
            num_units_on_truck += num_boxes_to_consume * num_units_per_box

            box_types_idx += 1

        return num_units_on_truck


# @leet end
