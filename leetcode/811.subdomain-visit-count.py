# @leet start
from collections import defaultdict


class Solution:
    def subdomainVisits(self, cpdomains: list[str]) -> list[str]:
        visit_counts: defaultdict[str, int] = defaultdict(int)

        for s in cpdomains:
            count, subdomain = s.split()
            count = int(count)

            while "." in subdomain:
                visit_counts[subdomain] += count
                subdomain = subdomain.split(".", 1)[1]

            visit_counts[subdomain] += count

        return [f"{count} {subdomain}" for subdomain, count in visit_counts.items()]


# @leet end
