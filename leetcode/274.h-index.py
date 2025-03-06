# @leet start
from collections import Counter


class Solution:
    def hIndex(self, citations: list[int]) -> int:
        # Find the largest h such that there are at least h papers with
        # h citations. First, count the number of papers that have a
        # given citation count.
        citation_counts = Counter(citations)

        # Keep track of the total number of papers counted while
        # iterating through counts in order of descending number of
        # paper citations. We do two checks in order as we iterate on a
        # given number of citations h:
        #
        # - if we have encountered total_paper_count papers and this
        #   total is greater than h, than these papers have citations of
        #   at least total_paper_count (comment below), which is greater
        #   than or equal to h and is the greatest attainable h-index
        # - if the first check is not met, we add the current count to
        #   the total paper count. If we have at least h papers, these
        #   papers have citations greater than or equal to h, and this
        #   is the greatest attainable h-index.
        #
        # If neither check is met, we continue iterating. Why do, in the
        # first check, all previously encountered papers have a citation
        # count of at least the number of encountered papers? If the
        # second check was not passed on the previous iteration then
        # total_paper_count < (previous) h. We know all of these papers
        # of citations of at least (previous) h though, therefore, they
        # have citations of at least total_paper_count.
        total_paper_count = 0

        for h, count in sorted(
            citation_counts.items(), key=lambda x: x[0], reverse=True
        ):
            if total_paper_count >= h:
                return total_paper_count

            total_paper_count += count

            if total_paper_count >= h:
                return h

        return total_paper_count


# @leet end
