# @leet start
import re


class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        # Strip out "."s and "+"s from the local name
        addresses: set[str] = set()

        for email in emails:
            local, domain = email.split("@")
            addresses.add(re.sub(r"\+.*|\.", "", local) + "@" + domain)

        return len(addresses)


# @leet end
