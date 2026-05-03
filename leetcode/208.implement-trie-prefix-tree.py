# @leet start
class Trie:

    def __init__(self):
        self.children: list[Trie | None] = [None] * 26
        self.terminates = False  # does word terminate here?

    @staticmethod
    def _get_char_idx(ch: str) -> int:
        return ord(ch) - ord("a")

    def _search_helper(self, s: str, require_terminate: bool):
        node = self

        for ch in s:
            idx = Trie._get_char_idx(ch)

            if not node.children[idx]:
                return False

            node = node.children[idx]

        return node.terminates or not require_terminate

    def insert(self, word: str) -> None:
        node = self

        for ch in word:
            idx = Trie._get_char_idx(ch)

            if not node.children[idx]:
                node.children[idx] = Trie()

            node = node.children[idx]

        node.terminates = True

    def search(self, word: str) -> bool:
        return self._search_helper(word, True)

    def startsWith(self, prefix: str) -> bool:
        return self._search_helper(prefix, False)


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @leet end
