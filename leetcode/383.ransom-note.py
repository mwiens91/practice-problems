# @leet start
from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_counter = Counter(magazine)

        for char, count in Counter(ransomNote).items():
            if count > magazine_counter[char]:
                return False

        return True
# @leet end
