# @leet start
from collections import Counter
import heapq


class Solution:
    def rearrangeBarcodes(self, barcodes: list[int]) -> list[int]:
        # Put barcode counts in a max-heap with two-tuples
        # (-count, barcode). I'm negating the counts here because the
        # heap algorithm that is being used assumes a min-heap.
        heap = [(-count, barcode) for barcode, count in Counter(barcodes).items()]

        heapq.heapify(heap)

        # Generate the new barcode ordering by using pairs of barcodes
        # consisting of the first and second most frequent barcodes
        # available, decreasing the count of each barcode we use as we
        # iterate
        new_barcodes = []

        while len(heap) >= 2:
            # Get the first two elements from the heap
            first_negative_count, first_barcode = heapq.heappop(heap)
            second_negative_count, second_barcode = heapq.heappop(heap)

            # Place the barcodes in the new ordering. The heap algorithm
            # guarantees we don't have adjacencies.
            new_barcodes += [first_barcode, second_barcode]

            # Put the elements back on the heap with a reduced count
            first_negative_count += 1
            second_negative_count += 1

            if first_negative_count:
                heapq.heappush(heap, (first_negative_count, first_barcode))

            if second_negative_count:
                heapq.heappush(heap, (second_negative_count, second_barcode))

        # If there is an element left on the heap, add it to the barcode
        # ordering
        if heap:
            new_barcodes.append(heap[0][1])

        return new_barcodes


# @leet end
