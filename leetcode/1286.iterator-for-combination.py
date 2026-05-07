# @leet start
class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.s = characters
        self.k = combinationLength
        self.n = len(characters)
        self.idxs = list(range(combinationLength))
        self.temp = 0

    def next(self) -> str:
        res = "".join(self.s[i] for i in self.idxs)
        self.idxs[-1] += 1

        i = self.k - 1

        while i >= 0 and self.idxs[i] > i + self.n - self.k:
            i -= 1
            self.idxs[i] += 1

        i += 1

        while 0 < i < self.k:
            self.idxs[i] = self.idxs[i - 1] + 1
            i += 1

        return res

    def hasNext(self) -> bool:
        return self.idxs[-1] < self.n


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
# @leet end
