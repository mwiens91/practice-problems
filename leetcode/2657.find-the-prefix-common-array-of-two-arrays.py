# @leet start
class Solution:
    def findThePrefixCommonArray(self, A: list[int], B: list[int]) -> list[int]:
        # Find the prefix intersection lengths of A and B
        result: list[int] = []

        set_a: set[int] = set()
        set_b: set[int] = set()

        for num_a, num_b in zip(A, B):
            set_a.add(num_a)
            set_b.add(num_b)

            result.append(len(set_a & set_b))

        return result


# @leet end
