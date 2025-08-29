# @leet start
from collections import defaultdict


class Solution:
    def findDuplicate(self, paths: list[str]) -> list[list[str]]:
        content_to_paths_dict: defaultdict[str, list[str]] = defaultdict(list)

        for listing in paths:
            chunks = listing.split()
            dir_path = chunks[0]

            for chunk in chunks[1:]:
                open = chunk.index("(")

                filename = chunk[:open]
                content = chunk[open:-1]

                content_to_paths_dict[content].append(dir_path + "/" + filename)

        return [l for l in content_to_paths_dict.values() if len(l) > 1]


# @leet end
