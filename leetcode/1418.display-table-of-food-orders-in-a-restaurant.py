# @leet start
from collections import defaultdict


class Solution:
    def displayTable(self, orders: list[list[str]]) -> list[list[str]]:
        items: set[str] = set()
        table_counts: defaultdict[int, defaultdict[str, int]] = defaultdict(
            lambda: defaultdict(int)
        )

        for _, table_num, item in orders:
            items.add(item)
            table_counts[int(table_num)][item] += 1

        sorted_items = sorted(items)
        res = [["Table"] + sorted_items]

        for table_num in sorted(table_counts.keys()):
            res.append(
                [str(table_num)]
                + [str(table_counts[table_num][item]) for item in sorted_items]
            )

        return res


# @leet end
